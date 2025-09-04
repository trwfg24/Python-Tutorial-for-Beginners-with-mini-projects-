# Bài 11: Phạm Vi Biến (Variable Scope) trong Python

## Mục tiêu học tập

Trong bài học này, bạn sẽ học về:

- Hiểu về phạm vi biến (scope) trong Python
- Phân biệt giữa biến toàn cục (global) và biến cục bộ (local)
- Sử dụng từ khóa `global` và `nonlocal`
- Áp dụng kiến thức về scope trong dự án game Rock-Paper-Scissors nâng cao

## Nội dung chi tiết

### 1. Phạm Vi Biến (Variable Scope)

Phạm vi biến quyết định nơi mà một biến có thể được truy cập trong chương trình.

#### Các loại phạm vi:

- **Phạm vi toàn cục (Global Scope)**: Biến được định nghĩa ở cấp độ module
- **Phạm vi cục bộ (Local Scope)**: Biến được định nghĩa bên trong hàm
- **Phạm vi phi cục bộ (Nonlocal Scope)**: Biến trong hàm lồng nhau

### 2. Biến toàn cục (Global Variables)

```python
name = "Dave"  # Biến toàn cục
count = 1      # Biến toàn cục

def another():
    global count  # Sử dụng từ khóa global để sửa đổi biến toàn cục
    count += 2
    print(count)
```

### 3. Biến cục bộ (Local Variables)

```python
def another():
    color = "blue"  # Biến cục bộ - chỉ tồn tại trong hàm này
```

### 4. Từ khóa `nonlocal`

```python
def another():
    color = "blue"

    def greeting(name):
        nonlocal color  # Truy cập biến của hàm cha
        color = "red"   # Thay đổi giá trị biến của hàm cha
```

## Files trong bài học

### `scope.py`

File demo minh họa các khái niệm về phạm vi biến:

- Biến toàn cục `name` và `count`
- Sử dụng `global` để thay đổi biến toàn cục
- Sử dụng `nonlocal` trong hàm lồng nhau
- Biến cục bộ `color`

### `rps4.py`

Phiên bản nâng cao của game Rock-Paper-Scissors với:

- Sử dụng biến toàn cục `game_count` để đếm số game đã chơi
- Từ khóa `global` để cập nhật biến đếm
- Hàm lồng nhau `decide_winner()` bên trong `play_rps()`
- Sử dụng Enum để định nghĩa các lựa chọn
- Đệ quy để chơi lại game

## Khái niệm quan trọng

### LEGB Rule

Python tìm kiếm biến theo thứ tự:

1. **L**ocal - Phạm vi cục bộ
2. **E**nclosing - Phạm vi hàm bao quanh
3. **G**lobal - Phạm vi toàn cục
4. **B**uilt-in - Phạm vi tích hợp sẵn

### Best Practices

1. **Hạn chế sử dụng biến toàn cục**: Chỉ dùng khi thực sự cần thiết
2. **Ưu tiên truyền tham số**: Thay vì dùng biến toàn cục
3. **Đặt tên biến rõ ràng**: Để phân biệt scope
4. **Sử dụng `global` và `nonlocal` cẩn thận**: Chỉ khi cần thay đổi biến bên ngoài

## Lưu ý quan trọng

- **Biến toàn cục** có thể được đọc từ bất kỳ đâu nhưng cần `global` để thay đổi
- **Biến cục bộ** chỉ tồn tại trong phạm vi hàm
- **`nonlocal`** chỉ hoạt động trong hàm lồng nhau
- **Tránh lạm dụng** biến toàn cục vì có thể gây khó hiểu và debug
