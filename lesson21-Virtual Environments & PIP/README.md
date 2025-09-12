# Lesson 21: Virtual Environments & PIP

## Mô tả bài học

Bài học này giới thiệu về **Virtual Environments (Môi trường ảo)** và **PIP (Python Package Installer)** - hai công cụ quan trọng trong phát triển ứng dụng Python. Thông qua việc xây dựng một ứng dụng thời tiết đơn giản, bạn sẽ học cách quản lý các gói thư viện và tạo môi trường phát triển độc lập.

## Nội dung chính

### 1. Virtual Environments (Môi trường ảo)

- **Khái niệm**: Môi trường ảo là một không gian độc lập cho mỗi dự án Python
- **Lợi ích**:
  - Tránh xung đột giữa các phiên bản thư viện khác nhau
  - Giữ cho hệ thống Python chính sạch sẽ
  - Dễ dàng chia sẻ dự án với người khác
  - Quản lý dependencies cho từng dự án riêng biệt

### 2. PIP (Python Package Installer)

- **Khái niệm**: Công cụ quản lý gói thư viện Python
- **Chức năng chính**:
  - Cài đặt thư viện từ PyPI (Python Package Index)
  - Cập nhật và gỡ bỏ thư viện
  - Quản lý danh sách dependencies

### 3. Dự án thực hành: Ứng dụng thời tiết

#### Chức năng

- Lấy thông tin thời tiết hiện tại của một thành phố
- Sử dụng OpenWeatherMap API
- Hiển thị nhiệt độ, cảm giác nhiệt độ và mô tả thời tiết

#### Thư viện được sử dụng

1. **requests**: Thực hiện HTTP requests để gọi API
2. **python-dotenv**: Quản lý biến môi trường từ file `.env`
3. **pprint**: Hiển thị dữ liệu JSON một cách đẹp mắt (tích hợp sẵn)

## Cài đặt và chạy dự án

### Bước 1: Tạo Virtual Environment

```bash
# Tạo môi trường ảo
python -m venv lesson21_env

# Kích hoạt môi trường ảo (Windows)
lesson21_env\Scripts\activate
```

### Bước 2: Cài đặt dependencies

```bash
# Cài đặt từ file requirements.txt
pip install -r requirments.txt

# Hoặc cài đặt từng thư viện
pip install requests python-dotenv
```

### Bước 3: Cấu hình API Key

1. Tạo tài khoản tại [OpenWeatherMap](https://openweathermap.org/api)
2. Lấy API key miễn phí
3. Tạo file `.env` trong thư mục dự án:

```
API_KEY=your_api_key_here
```

### Bước 4: Chạy ứng dụng

```bash
python weather.py
```

## Cấu trúc file

```
lesson21-Virtual Environments & PIP/
├── weather.py          # File chính của ứng dụng
├── requirments.txt     # Danh sách dependencies
├── .env               # File chứa API key (cần tạo)
└── README.md          # File mô tả dự án
```

## Kiến thức rút ra

### Các lệnh PIP quan trọng

```bash
pip install package_name        # Cài đặt gói
pip install package_name==1.0.0 # Cài đặt phiên bản cụ thể
pip list                        # Liệt kê các gói đã cài
pip show package_name           # Thông tin chi tiết về gói
pip freeze                      # Xuất danh sách gói với phiên bản
pip freeze > requirements.txt   # Tạo file requirements.txt
pip uninstall package_name      # Gỡ bỏ gói
```

### Quản lý Virtual Environment

```bash
# Tạo môi trường ảo
python -m venv env_name

# Kích hoạt
source env_name/bin/activate    # macOS/Linux
env_name\Scripts\activate       # Windows

# Tắt môi trường ảo
deactivate

# Xóa môi trường ảo
rm -rf env_name                 # macOS/Linux
rmdir /s env_name              # Windows
```

## Lưu ý quan trọng

1. **Luôn sử dụng Virtual Environment** cho mỗi dự án Python
2. **File .env không nên commit** vào version control (thêm vào .gitignore)
3. **Requirements.txt** giúp người khác dễ dàng cài đặt dependencies
4. **Kích hoạt môi trường ảo** trước khi làm việc với dự án
5. **Cập nhật requirements.txt** khi thêm thư viện mới
