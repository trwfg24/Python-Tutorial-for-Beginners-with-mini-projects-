# Lesson 04: Kiểu Dữ Liệu trong Python (Data Types)

## Mục tiêu học tập

Trong bài học này, bạn sẽ học về các kiểu dữ liệu cơ bản trong Python và cách sử dụng chúng.

## Nội dung bài học

### 1. Kiểu Dữ Liệu Chuỗi (String)

#### Khởi tạo chuỗi

```python
# Gán trực tiếp
first = "Truong"
last = "Nguyen"

# Sử dụng constructor
pizza = str("Pepperoni")
```

#### Các thao tác với chuỗi

- **Nối chuỗi (Concatenation)**: Sử dụng toán tử `+`
- **Gán tích lũy**: Sử dụng toán tử `+=`
- **Ép kiểu số thành chuỗi**: Sử dụng `str()`

#### Chuỗi nhiều dòng

```python
multiline = """
Đây là chuỗi
nhiều dòng
"""
```

#### Ký tự đặc biệt (Escape Characters)

- `\'` - Dấu nháy đơn
- `\t` - Tab
- `\n` - Xuống dòng
- `\\` - Dấu gạch chéo ngược

#### Các phương thức chuỗi quan trọng

- `lower()` - Chuyển thành chữ thường
- `upper()` - Chuyển thành chữ hoa
- `title()` - Viết hoa chữ cái đầu
- `replace()` - Thay thế chuỗi con
- `strip()` - Loại bỏ khoảng trắng
- `startswith()` - Kiểm tra bắt đầu bằng
- `endswith()` - Kiểm tra kết thúc bằng

#### Định dạng chuỗi

- `center()` - Căn giữa
- `ljust()` - Căn trái
- `rjust()` - Căn phải

#### Truy cập ký tự trong chuỗi

- Chỉ số dương: `string[0]`, `string[1]`
- Chỉ số âm: `string[-1]` (ký tự cuối)
- Cắt chuỗi: `string[start:end]`

### 2. Kiểu Dữ Liệu Boolean

```python
myvalue = True
x = bool(False)
```

- Chỉ có hai giá trị: `True` và `False`
- Được sử dụng trong các phép so sánh và điều kiện

### 3. Kiểu Dữ Liệu Số

#### Số nguyên (Integer)

```python
price = 100
best_price = int(80)
```

#### Số thực (Float)

```python
gpa = 3.28
y = float(1.14)
```

#### Số phức (Complex)

```python
comp_value = 5 + 3j
print(comp_value.real)  # Phần thực
print(comp_value.imag)  # Phần ảo
```

### 4. Hàm tích hợp cho số

- `abs()` - Giá trị tuyệt đối
- `round()` - Làm tròn
- `int()` - Chuyển đổi sang số nguyên
- `float()` - Chuyển đổi sang số thực

### 5. Module Math

```python
import math

math.pi          # Số π
math.sqrt(64)    # Căn bậc hai
math.ceil(gpa)   # Làm tròn lên
math.floor(gpa)  # Làm tròn xuống
```

### 6. Kiểm tra kiểu dữ liệu

```python
# Sử dụng type()
print(type(variable))

# Sử dụng isinstance()
print(isinstance(variable, str))
```

## Ví dụ thực tế

### Xây dựng menu nhà hàng

```python
title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(16, '.') + '$1'.rjust(4))
```

## Lưu ý quan trọng

1. **Ép kiểu dữ liệu**: Cần cẩn thận khi chuyển đổi giữa các kiểu dữ liệu
2. **Lỗi thường gặp**: Không thể chuyển chuỗi không phải số thành số
3. **Chuỗi bất biến**: Các phương thức chuỗi không thay đổi chuỗi gốc mà trả về chuỗi mới

## Bài tập

1. Tạo một chương trình tính toán điểm trung bình và hiển thị kết quả đẹp mắt
2. Viết chương trình xử lý tên người dùng (loại bỏ khoảng trắng, viết hoa chữ cái đầu)
3. Tạo một menu đơn giản cho quán cà phê

## File thực hành

- `data_type.py` - Chứa tất cả các ví dụ và bài tập thực hành
