# DATATHON
Datathon VinUni 2026
Cấu trúc thư mục  
```
├── data/
│   ├── raw/                 # Chứa nguyên bản 15 file CSV vừa tải về. KHÔNG sửa trực tiếp các file này.
│   └── processed/           # Chứa các file dữ liệu đã qua xử lý (merge, clean) để load nhanh hơn.
├── notebooks/
│   ├── 00_data_cleaning.ipynb
│   ├── 01_mcq_calculations.ipynb # Code tính toán để trả lời 10 câu hỏi Phần 1.
│   ├── 02_eda_and_storytelling.ipynb # Code vẽ biểu đồ, phân tích 4 cấp độ (Descriptive đến Prescriptive) cho Phần 2.
│   └── 03_sales_forecasting.ipynb # Code huấn luyện mô hình dự báo Revenue và vẽ biểu đồ giải thích (SHAP) cho Phần 3.
├── src/                     # (Tuỳ chọn) Chứa các file .py chứa hàm tự viết dùng chung (ví dụ: hàm merge data, hàm tính MAE/RMSE).
├── report/
│   ├── main.tex             # File mã nguồn báo cáo theo template NeurIPS.
│   ├── references.bib       # File quản lý tài liệu tham khảo cho báo cáo.
│   └── figures/             # Thư mục lưu các biểu đồ xuất ra từ file notebook để chèn vào báo cáo.
├── submissions/
│   ├── submission_v1.csv    # Các version file nộp thử nghiệm.
│   ├── experiments_log.csv  # Lịch sử nộp bài và các thông số
│   └── final_submission.csv # File nộp chính thức lên hệ thống Kaggle.
├── README.md                # BẮT BUỘC: Mô tả cấu trúc thư mục và hướng dẫn chạy code.
└── requirements.txt         # File khai báo các thư viện môi trường để đảm bảo tính tái lập.
```
