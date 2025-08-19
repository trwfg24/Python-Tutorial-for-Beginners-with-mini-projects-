# Lesson 06: List và Tuple trong Python

Trong bài học này, bạn sẽ học về List và Tuple - hai kiểu dữ liệu quan trọng trong Python.

## Nội dung bài học

### 1. Khai báo và khởi tạo List

- Tạo list chứa các kiểu dữ liệu khác nhau: strings, numbers, boolean
- Tạo list rỗng
- Sử dụng constructor `list()`

### 2. Truy cập phần tử trong List

- Truy cập bằng chỉ số (index): `users[0]`, `users[-2]`
- Tìm vị trí phần tử: `index()`
- Kiểm tra phần tử có tồn tại: `in` operator
- Slicing (cắt list): `users[0:2]`, `users[1:]`, `users[-3:-1]`

### 3. Các phương thức thêm phần tử

- `append()`: Thêm một phần tử vào cuối list
- `+=`: Thêm phần tử bằng toán tử
- `extend()`: Thêm nhiều phần tử từ iterable khác
- `insert()`: Thêm phần tử tại vị trí chỉ định
- Slicing assignment: `users[2:2] = ['Eddie', 'Alex']`

### 4. Các phương thức xóa phần tử

- `remove()`: Xóa phần tử theo giá trị
- `pop()`: Xóa và trả về phần tử cuối cùng
- `del`: Xóa phần tử theo chỉ số
- `clear()`: Xóa tất cả phần tử

### 5. Sắp xếp và đảo ngược

- `sort()`: Sắp xếp list tại chỗ
- `sort(key=str.lower)`: Sắp xếp không phân biệt hoa thường
- `reverse()`: Đảo ngược thứ tự
- `sorted()`: Tạo list mới đã sắp xếp

### 6. Sao chép List

- `copy()`: Tạo bản sao
- `list()`: Tạo list mới từ list hiện tại
- Slicing `[:]`: Sao chép bằng cắt toàn bộ

### 7. Tuple

- Khái niệm và cách khai báo tuple
- Chuyển đổi giữa list và tuple
- Unpacking tuple với `*` operator
- Phương thức `count()` của tuple
