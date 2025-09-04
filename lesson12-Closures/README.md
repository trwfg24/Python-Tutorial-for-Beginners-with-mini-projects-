# Bài 12: Closures (Bao đóng) trong Python

## Mục tiêu học tập

Trong bài học này, bạn sẽ học về:

- Hiểu khái niệm Closures (Bao đóng) trong Python
- Cách tạo và sử dụng closures
- Ứng dụng closures trong việc lưu trữ trạng thái
- Kết hợp closures với nonlocal để quản lý dữ liệu
- Áp dụng closures trong dự án game Rock-Paper-Scissors nâng cao

## Nội dung chi tiết

### 1. Closures là gì?

**Closure** (Bao đóng) là một hàm có khả năng truy cập vào phạm vi (scope) của hàm cha ngay cả sau khi hàm cha đã kết thúc thực thi.

#### Đặc điểm của Closures:

- Hàm con được định nghĩa bên trong hàm cha
- Hàm con sử dụng biến từ phạm vi của hàm cha
- Hàm cha trả về hàm con
- Biến của hàm cha được "nhớ" trong closure

### 2. Cấu trúc cơ bản của Closure

```python
def parent_function(parameter):
    # Biến trong phạm vi hàm cha
    local_variable = parameter

    def child_function():
        # Truy cập biến của hàm cha
        nonlocal local_variable
        # Thực hiện các thao tác
        return local_variable

    return child_function  # Trả về hàm con
```

### 3. Lợi ích của Closures

- **Lưu trữ trạng thái**: Giữ dữ liệu giữa các lần gọi hàm
- **Đóng gói dữ liệu**: Tạo ra các hàm có dữ liệu riêng biệt
- **Factory functions**: Tạo ra nhiều hàm tương tự với cấu hình khác nhau
- **Thay thế cho class**: Trong một số trường hợp đơn giản

## Files trong bài học

### `closures.py`

File demo minh họa khái niệm closure cơ bản:

```python
def parent_function(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1
        # Logic game với coins
    return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)
```

**Tính năng:**

- Tạo ra các game instance riêng biệt cho từng người chơi
- Mỗi closure có trạng thái coins riêng
- Sử dụng `nonlocal` để thay đổi biến của hàm cha
- Theo dõi số coins còn lại của từng người

### `rps5.py`

Phiên bản Rock-Paper-Scissors sử dụng closures:

```python
def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins, game_count
        # Game logic với state tracking

    return play_rps

play = rps()
play()
```

**Cải tiến so với phiên bản trước:**

- Đóng gói tất cả game state trong closure
- Theo dõi số lần thắng của player và computer
- Quản lý game count bằng closure
- Tạo game instance có thể tái sử dụng

## Khái niệm quan trọng

### Closure vs Class

| Closure                    | Class                         |
| -------------------------- | ----------------------------- |
| Đơn giản, ít code          | Phức tạp hơn, nhiều tính năng |
| Phù hợp cho logic đơn giản | Phù hợp cho object phức tạp   |
| Hiệu suất cao              | Tính năng OOP đầy đủ          |
| Ít memory overhead         | Nhiều method và attribute     |

### Closure vs Global Variables

| Closure            | Global Variables              |
| ------------------ | ----------------------------- |
| Encapsulation tốt  | Có thể bị truy cập từ mọi nơi |
| Multiple instances | Chỉ một instance              |
| Thread-safe        | Cần cẩn thận với threading    |
| Clean code         | Có thể gây pollution          |

## Lưu ý quan trọng

### Best Practices:

- **Sử dụng closures** khi cần lưu trữ state đơn giản
- **Tránh closures phức tạp** - hãy dùng class thay thế
- **Cẩn thận với memory** - closures giữ reference đến outer scope
- **Sử dụng nonlocal** để thay đổi biến outer scope

### Khi nào sử dụng Closures:

✅ **Tốt cho:**

- Factory functions
- Event handlers
- Decorators
- Simple state management

❌ **Không tốt cho:**

- Complex objects với nhiều methods
- Inheritance relationships
- Large state objects

## Debugging Closures

```python
# Kiểm tra closure variables
def outer():
    x = 10
    def inner():
        return x
    print(inner.__closure__)  # Xem closure variables
    return inner
```

## Thuật ngữ quan trọng

- **Closure**: Bao đóng - hàm có thể truy cập scope của hàm cha
- **Enclosing scope**: Phạm vi bao quanh
- **Free variables**: Biến từ outer scope được sử dụng trong inner function
- **Factory function**: Hàm tạo ra các hàm khác
- **State preservation**: Lưu trữ trạng thái giữa các lần gọi hàm
