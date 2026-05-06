# LAB 2: API + FIREBASE
# Note App
Một ứng dụng ghi chú tối giản áp dụng kiến trúc tách biệt Frontend/Backend, tích hợp hệ thống xác thực và cơ sở dữ liệu thời gian thực.

## 1. Thông tin sinh viên
* **Họ và tên:** Đỗ Quốc Đại
* **MSSV:** 24120030
* **Lớp:** 24CTT3


## 2. Tổ chức kiến trúc

*   **Frontend:** Xây dựng bằng HTML/JS thuần kết hợp Tailwind CSS (qua CDN), quản lý phiên đăng nhập trực tiếp qua Firebase Authentication.
*   **Backend:** Phát triển trên nền tảng FastAPI, đảm nhận vai trò trung gian giao tiếp an toàn với Firebase Firestore.

## 3. Cài đặt môi trường (Environment Setup)

Yêu cầu hệ thống đã cài đặt Python. Để thiết lập môi trường cô lập cho dự án:

```bash
# Tạo và kích hoạt môi trường ảo
python -m venv venv
source venv/bin/activate  # Đối với Windows: venv/Scripts/activate

# Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt
```

## 4. Hướng dẫn chạy Backend

Lấy key firebase admin đặt vào file **firebase_admin.json**

Mở terminal, đảm bảo môi trường ảo đang được kích hoạt và khởi động máy chủ FastAPI:

```bash
uvicorn backend.main:app --reload --port 8000
```
API Server sẽ khởi chạy. Nếu bạn sử dụng GitHub Codespaces, hãy nhớ chuyển Port 8000 sang trạng thái **Public** để Frontend có thể gọi API.

## 5. Hướng dẫn chạy Frontend

Lấy key firebase client đặt vào file **firebase_client.js**

Mở một cửa sổ terminal mới, điều hướng vào thư mục chứa giao diện và khởi tạo một web server cục bộ:

```bash
cd frontend
npx serve -p 5500
```
Sau khi server báo thành công, hãy truy cập vào đường dẫn được cung cấp (ví dụ: `http://localhost:5500`) trên trình duyệt để trải nghiệm ứng dụng.

## 6. Video Demo

**Đường dẫn Video Demo:**
