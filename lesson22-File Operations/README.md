# Bài 22: Thao Tác Với File (File Operations)

## Mô Tả

Bài học này hướng dẫn cách thực hiện các thao tác cơ bản với file trong Python, bao gồm đọc, ghi, tạo và xóa file.

## Nội Dung Học

### 1. Các Chế Độ Mở File

Python hỗ trợ 4 chế độ chính khi làm việc với file:

- **`r`** - Read (Đọc): Mở file để đọc, báo lỗi nếu file không tồn tại
- **`a`** - Append (Thêm): Thêm nội dung vào cuối file, tự động tạo file nếu chưa tồn tại
- **`w`** - Write (Ghi đè): Ghi đè toàn bộ nội dung file, tự động tạo file nếu chưa tồn tại
- **`x`** - Create (Tạo mới): Tạo file mới, báo lỗi nếu file đã tồn tại

### 2. Các Kỹ Thuật Được Học

#### Đọc File

```python
# Mở và đọc toàn bộ file
f = open("names.txt")
print(f.read())
f.close()

# Đọc một số ký tự nhất định
print(f.read(4))

# Đọc từng dòng
print(f.readline())

# Sử dụng vòng lặp để đọc từng dòng
for line in f:
    print(line)
```

#### Xử Lý Lỗi Khi Đọc File

```python
try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("File bạn muốn đọc không tồn tại")
finally:
    f.close()
```

#### Thêm Nội Dung Vào File

```python
f = open("names.txt", "a")
f.write("Neil")
f.close()
```

#### Ghi Đè Nội Dung File

```python
f = open("context.txt", "w")
f.write("Tôi đã xóa toàn bộ nội dung cũ")
f.close()
```

#### Tạo File Mới

```python
# Cách 1: Sử dụng chế độ "w"
f = open("name_list.txt", "w")
f.close()

# Cách 2: Sử dụng chế độ "x" (an toàn hơn)
import os
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
```

#### Xóa File

```python
import os
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("File bạn muốn xóa không tồn tại")
```

#### Sử Dụng Context Manager (Cách Tốt Nhất)

```python
# Tự động đóng file sau khi sử dụng
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
```

### 3. Files Trong Dự Án

- **`file.py`**: File Python chính chứa tất cả các ví dụ
- **`names.txt`**: File chứa danh sách tên để thực hành đọc/ghi
- **`more_names.txt`**: File bổ sung chứa danh sách tên
- **`context.txt`**: File để thực hành ghi đè nội dung
- **`name_list.txt`**: File được tạo động trong quá trình chạy chương trình

### 4. Kiến Thức Quan Trọng

#### Tại Sao Phải Đóng File?

- Giải phóng bộ nhớ hệ thống
- Đảm bảo dữ liệu được lưu đúng cách
- Tránh lỗi khi file đang được sử dụng

#### Context Manager (`with` statement)

- Tự động đóng file ngay cả khi có lỗi xảy ra
- Cách viết code sạch và an toàn hơn
- Không cần phải nhớ gọi `close()`

#### Xử Lý Lỗi

- Luôn kiểm tra file có tồn tại trước khi xóa
- Sử dụng `try-except` khi đọc file
- Sử dụng `finally` để đảm bảo file được đóng

### 5. Ứng Dụng Thực Tế

- Đọc file cấu hình
- Lưu trữ dữ liệu người dùng
- Ghi log ứng dụng
- Xử lý dữ liệu từ file CSV, TXT
- Sao lưu và phục hồi dữ liệu

### 6. Lưu Ý Quan Trọng

- Luôn sử dụng `with` statement khi có thể
- Kiểm tra sự tồn tại của file trước khi thao tác
- Xử lý ngoại lệ một cách phù hợp
- Đóng file sau khi sử dụng (nếu không dùng `with`)
- Cẩn thận với chế độ "w" vì nó sẽ xóa toàn bộ nội dung cũ
