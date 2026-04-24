"""
ENSEMBLE WEIGHT OPTIMIZATION
Tìm trọng số tối ưu cho 3 model: XGBoost, LightGBM, Prophet
Các phương pháp:
  1. Grid Search (brute-force)
  2. NNLS - Non-Negative Least Squares
  3. scipy.optimize.minimize (Nelder-Mead)
  4. Optuna (Bayesian Optimization)
"""
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.optimize import nnls
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)

def print_metrics(y_true, y_pred, label):
    print(f"[{label}] MAE={mae(y_true,y_pred):,.2f} | RMSE={rmse(y_true,y_pred):,.2f} | "
          f"R²={1 - np.sum((y_true-y_pred)**2)/np.sum((y_true-np.mean(y_true))**2):.4f}")

def grid_search_weights(preds_list, y_true, metric="rmse", step=0.05):
    """
    Duyệt lưới trọng số [0, 1] với bước = step.
    preds_list: list 3 mảng dự đoán [pred_xgb, pred_lgb, pred_prophet]
    metric: "rmse" hoặc "mae"
    """
    score_fn = rmse if metric == "rmse" else mae
    best_score = np.inf
    best_w = (1/3, 1/3, 1/3)

    steps = np.arange(0, 1 + step, step)
    for wa in steps:
        for wb in steps:
            wc = 1.0 - wa - wb
            if wc < 0 or wc > 1:
                continue
            ensemble = wa * preds_list[0] + wb * preds_list[1] + wc * preds_list[2]
            score = score_fn(y_true, ensemble)
            if score < best_score:
                best_score = score
                best_w = (round(wa, 4), round(wb, 4), round(wc, 4))

    return best_w, best_score

def nnls_weights(preds_list, y_true):
    """
    Non-Negative Least Squares: tìm w >= 0 tối thiểu ||Xw - y||²
    Sau đó chuẩn hóa tổng = 1.
    """
    X = np.column_stack(preds_list)
    w, _ = nnls(X, y_true)
    if w.sum() > 0:
        w = w / w.sum()
    return tuple(np.round(w, 6))

def scipy_optimize_weights(preds_list, y_true, metric="rmse"):
    """
    Minimize metric (MAE / RMSE) bằng Nelder-Mead.
    Ràng buộc: w_i >= 0, sum(w_i) = 1.
    """
    score_fn = rmse if metric == "rmse" else mae

    def objective(w):
        exp_w = np.exp(w - np.max(w))
        w_norm = exp_w / exp_w.sum()
        ensemble = sum(w_norm[i] * preds_list[i] for i in range(len(preds_list)))
        return score_fn(y_true, ensemble)

    w0 = np.zeros(len(preds_list))  
    result = minimize(objective, w0, method="Nelder-Mead",
                      options={"maxiter": 10000, "xatol": 1e-8, "fatol": 1e-8})

    exp_w = np.exp(result.x - np.max(result.x))
    w_final = exp_w / exp_w.sum()
    return tuple(np.round(w_final, 6)), result.fun

def optuna_optimize_weights(preds_list, y_true, metric="rmse", n_trials=500):
    """
    Dùng Optuna để tìm trọng số tối ưu bằng Bayesian Optimization.
    """
    try:
        import optuna
        optuna.logging.set_verbosity(optuna.logging.WARNING)
    except ImportError:
        print("Optuna chưa được cài. Chạy: pip install optuna")
        return None, None

    score_fn = rmse if metric == "rmse" else mae
    n = len(preds_list)

    def objective(trial):
        raw = [trial.suggest_float(f"w{i}", 0.0, 1.0) for i in range(n)]
        total = sum(raw)
        if total == 0:
            return float("inf")
        w = [r / total for r in raw]
        ensemble = sum(w[i] * preds_list[i] for i in range(n))
        return score_fn(y_true, ensemble)

    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=n_trials, show_progress_bar=False)

    best = study.best_params
    raw = [best[f"w{i}"] for i in range(n)]
    total = sum(raw)
    w_final = tuple(np.round(r / total, 6) for r in raw)
    return w_final, study.best_value

def find_best_ensemble_weights(
    pred_xgb, pred_lgb, pred_prophet,
    y_true,
    target_name="Revenue",
    metric="rmse",
    grid_step=0.05,
    optuna_trials=300
):
    """
    Chạy tất cả 4 phương pháp và so sánh kết quả.

    Trả về dict: {method: (weights, score)}
    weights = (w_xgb, w_lgb, w_prophet)
    """
    preds = [pred_xgb, pred_lgb, pred_prophet]
    results = {}

    # --- Baseline: Equal weights ---
    ens_equal = (pred_xgb + pred_lgb + pred_prophet) / 3
    score_fn = rmse if metric == "rmse" else mae
    results["equal"] = ((1/3, 1/3, 1/3), score_fn(y_true, ens_equal))

    # --- Method 1: Grid Search ---
    w1, s1 = grid_search_weights(preds, y_true, metric=metric, step=grid_step)
    results["grid_search"] = (w1, s1)

    # --- Method 2: NNLS ---
    w2 = nnls_weights(preds, y_true)
    ens2 = w2[0]*pred_xgb + w2[1]*pred_lgb + w2[2]*pred_prophet
    results["nnls"] = (w2, score_fn(y_true, ens2))

    # --- Method 3: Scipy Minimize ---
    w3, s3 = scipy_optimize_weights(preds, y_true, metric=metric)
    results["scipy_minimize"] = (w3, s3)

    # --- Method 4: Optuna ---
    w4, s4 = optuna_optimize_weights(preds, y_true, metric=metric, n_trials=optuna_trials)
    if w4 is not None:
        results["optuna"] = (w4, s4)

    # --- In kết quả ---
    print(f"  ENSEMBLE WEIGHT OPTIMIZATION — {target_name} (metric={metric.upper()})")
    print(f"  {'Method':<20} {'XGB':>8} {'LGB':>8} {'Prophet':>9} {'Score':>12}")
    for method, (w, score) in results.items():
        print(f"  {method:<20} {w[0]:>8.4f} {w[1]:>8.4f} {w[2]:>9.4f} {score:>12,.2f}")

    # Tìm method tốt nhất
    best_method = min(results, key=lambda k: results[k][1])
    best_w, best_score = results[best_method]
    print(f"\nBest: [{best_method}]  XGB={best_w[0]:.4f} | LGB={best_w[1]:.4f} | "
          f"Prophet={best_w[2]:.4f}  |  {metric.upper()}={best_score:,.2f}\n")

    return results, best_w