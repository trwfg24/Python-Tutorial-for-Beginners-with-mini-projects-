# Bài 10: Đệ Quy và Ứng Dụng Nâng Cao

## Tổng Quan

Bài học này tập trung vào khái niệm **đệ quy (recursion)** trong Python và ứng dụng các kiến thức đã học vào việc xây dựng một trò chơi hoàn chỉnh.

## Nội Dung Kiến Thức

### 1. Vòng Lặp While Nâng Cao (`exmple.py`)

- **Vòng lặp while với điều kiện boolean**: Sử dụng biến boolean để điều khiển vòng lặp
- **Lệnh break**: Thoát khỏi vòng lặp khi đạt điều kiện nhất định
- **Lệnh continue**: Bỏ qua phần còn lại của vòng lặp và tiếp tục với lần lặp tiếp theo
- **Biến đếm**: Sử dụng biến để theo dõi số lần lặp

```python
# Ví dụ: Đếm từ 1 đến 5 với break và continue
value = "y"
count = 0

while value:
    count += 1
    print(count)
    if count == 5:
        break  # Thoát vòng lặp khi count = 5
    else:
        value = 0
        continue  # Tiếp tục vòng lặp
```

### 2. Đệ Quy (Recursion) (`recursion.py`)

- **Khái niệm**: Hàm gọi chính nó với tham số khác nhau
- **Điều kiện dừng**: Điều kiện để kết thúc đệ quy (base case)
- **Trường hợp đệ quy**: Hàm gọi lại chính nó với tham số đã thay đổi

```python
def add_one(num):
    if num >= 9:        # Điều kiện dừng
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)  # Gọi đệ quy
```

**Ưu điểm của đệ quy:**

- Code ngắn gọn và dễ hiểu
- Phù hợp với các bài toán có cấu trúc lặp lại

**Nhược điểm:**

- Có thể gây tràn stack nếu đệ quy quá sâu
- Hiệu suất có thể không tối ưu

### 3. Trò Chơi Kéo Búa Bao Nâng Cao (`rps3.py`)

#### Các Khái Niệm Mới:

- **Enum (Enumeration)**: Tạo tập hợp các hằng số có tên
- **Xử lý input người dùng**: Kiểm tra và xác thực dữ liệu đầu vào
- **Đệ quy trong ứng dụng thực tế**: Sử dụng đệ quy để chơi lại game
- **Xử lý chuỗi nâng cao**: Sử dụng `replace()` để định dạng output

#### Chi Tiết Kỹ Thuật:

**1. Enum Class:**

```python
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
```

**2. Xác Thực Input:**

```python
if playerchoice not in ["1", "2", "3"]:
    print("You must enter 1, 2 or 3.")
    return play_rps()  # Đệ quy để yêu cầu nhập lại
```

**3. Logic Game:**

- So sánh lựa chọn của người chơi và máy tính
- Xác định người thắng theo luật kéo búa bao
- Hiển thị kết quả với emoji

**4. Chơi Lại:**

```python
if playgain.lower() == "y":
    return play_rps()  # Đệ quy để chơi lại
else:
    sys.exit("Bye! 👌")  # Thoát game
```

## Lưu Ý Quan Trọng

- **Đệ quy phải có điều kiện dừng** để tránh vòng lặp vô hạn
- **Kiểm tra input** luôn là thói quen tốt trong lập trình
- **Sử dụng Enum** giúp code dễ đọc và bảo trì hơn
- **Xử lý lỗi gracefully** để cải thiện trải nghiệm người dùng
