# DATATHON 2026 - VinUni  
# Tối ưu hóa vận hành E-Commerce: Phân tích Hành vi Khách hàng và Hệ Thống Dự báo Doanh thu

## Đội thi Data Manipulators
1. **Khoa Đào Ngọc Bích** - Nhóm trưởng  
Khoa học máy tính (Trường Đại học Công nghệ - ĐHQGHN)

2. **Đỗ Mai Hằng**  
Hệ thống thông tin (Trường Đại học Công nghệ - ĐHQGHN)

3. **Từ Thị Thu Uyên**  
Hệ thống thông tin quản lý (Học viện Tài chính)

## Mô tả
Dự báo nhu cầu chính xác là yếu tố then chốt để tối ưu hóa tồn kho và logistics cho doanh nghiệp thương mại điện tử thời trang tại Việt Nam. Báo cáo này kết hợp phân tích chuyên sâu (EDA) để khám phá hành vi mua sắm đặc thù trong các kỳ Tết và Mega-sale với hệ thống dự báo sử dụng Ensemble LightGBM, XGBoost và N-HiTS. Bằng cách khai thác hơn 80 đặc trưng sáng tạo như độ trễ lưu lượng web và chỉ số khuyến mãi, mô hình đạt độ chính xác cao.   

Kết quả không chỉ cung cấp con số dự báo mà còn là câu chuyện về dữ liệu, giúp doanh nghiệp chủ động lập kế hoạch logistics và khuyến mãi hiệu quả trên toàn quốc.

## Cấu trúc thư mục  
```
├── data/
│   ├── raw/                            # Chứa nguyên bản 15 file CSV vừa tải về.
│   └── processed/                      # Chứa các file dữ liệu đã qua xử lý (merge, clean).
├── notebooks/
│   ├── 00_data_cleaning.ipynb          # Làm sạch dữ liệu
│   ├── 01_mcq_calculations.ipynb       # Tính toán phần Câu hỏi Trắc nghiệm.
│   ├── 02_eda_and_storytelling.ipynb   # Phần 2: Trực quan hoá và Phân tích Dữ liệu.
│   └── 03_sales_forecasting.ipynb      # Phần 3: Mô hình Dự báo Doanh thu.
├── report/
│   ├── main.tex                        # Mã nguồn báo cáo theo template NeurIPS.
│   ├── references.bib                  # Tài liệu tham khảo cho báo cáo.
│   └── figures/                        # Biểu đồ chèn vào báo cáo.
├── submissions/
│   └── submission.csv                  # File nộp chính thức lên hệ thống Kaggle.
├── DASHBOARD.pbix                      # Phần 2: Biểu đồ được xử lý bằng PowerBI
├── README.md                           # BẮT BUỘC: Mô tả cấu trúc thư mục và hướng dẫn chạy code.
└── requirements.txt                    # File khai báo các thư viện môi trường để đảm bảo tính tái lập.
```

## Hướng dẫn cài đặt và chạy dự án
### Yêu cầu môi trường
- Python 3.10+
- RAM: ≥ 8GB (Khuyến nghị 16GB)

### 1. Clone repository về máy
```bash
git clone https://github.com/Jade2612/DATATHON.git
```
### 2. Cài đặt môi trường
```bash
python -m venv .venv
# Kích hoạt môi trường (Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```
### 3. Khởi chạy chương trình
* 'Run All' **00_data_cleaning.ipynb**
* **Phần 1:** 'Run All' **01_mcq_calculations.ipynb**
* **Phần 2:**  
'Run All' **02_eda_and_storytelling.ipynb**  
Mở **DASHBOARD.pbix**
* **Phần 3:** 'Run All' **03_sales_forecasting.ipynb**

## Tài liệu tham khảo

**1. Mô hình Học máy & Khoa học Dữ liệu (Machine Learning & Data Science)**
*   **Chen, T., & Guestrin, C. (2016).** *XGBoost: A Scalable Tree Boosting System*. KDD '16.
*   **Ke, G. et al. (2017).** *LightGBM: A Highly Efficient Gradient Boosting Decision Tree*. NeurIPS 30.
*   **Challu, C. et al. (2022).** *N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting*. NeurIPS 35.
*   **Hyndman, R. J., & Athanasopoulos, G. (2021).** *Forecasting: Principles and Practice* (3rd ed.). OTexts. [Link](https://otexts.com/fpp3/)
*   **Waller, M. A., & Fawcett, S. E. (2013).** *Data science, predictive analytics, and big data: a revolution that will transform supply chain design and management*. Journal of Business Logistics, 34(2), 77-84.

**2. Quản trị Chuỗi cung ứng & Vận hành (Supply Chain & Operations)**
*   **Fisher, M. L., & Raman, A. (1996).** *Reducing the cost of demand uncertainty through accurate response to early sales*. Operations Research, 44(1), 87-99.
*   **Cachon, G. P., & Swinney, R. (2009).** *Purchasing, pricing, and quick response in the presence of strategic consumers*. Management Science, 55(3), 497-511.
*   **Silver, E. A., Pyke, D. F., & Peterson, R. (1998).** *Inventory Management and Production Planning and Scheduling* (3rd ed.). John Wiley & Sons.
*   **Ghemawat, P., & Nueno, J. L. (2003).** *Zara: Fast Fashion*. Harvard Business School Case 703-497.

**3. Nghiệp vụ E-commerce & Báo cáo Thị trường (E-commerce & Market Insights)**
*   **Statista & VECOM. (2024).** *E-commerce Return Rates in Vietnam*. Statista Report.
*   **McKinsey Vietnam. (2023).** *Inventory Management Challenges in Vietnam Retail*. McKinsey & Company.
*   **NielsenIQ. (2024).** *Customer Retention in Vietnam Fashion E-com*. Nielsen Report.
*   **Harvard Business Review. (2022).** *Customer Segmentation for Profitability in Retail*. HBR.
*   **Journal of Retailing. (2023).** *Discount Strategies Impact on E-commerce*. Journal of Retailing.
*   **Chaffey, D. (2022).** *Digital Business and E-commerce Management* (7th ed.). Pearson Education.
*   **Momentum Works. (2023).** *E-commerce in Southeast Asia 2023*. Momentum Works Report.
*   **Nielsen Vietnam. (2021).** *Vietnam Consumer & Media View Report Q3 2021*. The Nielsen Company Vietnam.
*   **CBRE Vietnam. (2022).** *Vietnam Retail Market Overview 2022*. CBRE Research.

## License

Dự án này được phát triển phục vụ cuộc thi Datathon 2026.  
Mã nguồn này được cung cấp chỉ để tham khảo. Vui lòng tuân thủ chính sách liêm chính học thuật của trường bạn.