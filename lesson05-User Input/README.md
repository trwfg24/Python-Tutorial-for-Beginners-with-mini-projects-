# Lesson 05: Rock Paper Scissors Game

## Mô tả

Bài học này hướng dẫn tạo một trò chơi "Kéo Búa Bao" (Rock Paper Scissors) đơn giản, nơi người chơi đối đầu với máy tính.

## Khái niệm được học

### 1. Import Modules

```python
import sys
import random
from enum import Enum
```

- **sys**: Module hệ thống để thoát chương trình
- **random**: Module tạo số ngẫu nhiên
- **enum**: Module tạo enumeration (liệt kê)

### 2. Enum (Enumeration)

```python
class RPS(Enum):
    ROCK  = 1
    PAPER = 2
    SCISSORS = 3
```

- Enum giúp tạo ra các hằng số có tên có ý nghĩa
- Dễ đọc và bảo trì code hơn

### 3. Input và Type Conversion

```python
playerchoice = input('Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')
player = int(playerchoice)
```

- Nhận input từ người dùng
- Chuyển đổi string thành integer

### 4. Conditional Logic (Điều kiện)

```python
if player < 1 | player > 3:
    sys.exit('You must enter 1,2, or 3.')
```

- Kiểm tra input hợp lệ
- Thoát chương trình nếu input không đúng

### 5. Random Choice

```python
computerchoice = random.choice('123')
computer = int(computerchoice)
```

- Máy tính chọn ngẫu nhiên từ các lựa chọn

### 6. String Manipulation

```python
print('You chose ' + str(RPS(player)).replace('RPS.', '') + '.')
```

- Chuyển đổi enum thành string
- Sử dụng `replace()` để loại bỏ prefix không cần thiết

### 7. Game Logic

```python
if player == 1 and computer == 3:
    print('🎉You win!')
elif player == 2 and computer == 1:
    print('🎉You win!')
elif player == 3 and computer == 2:
    print('🎉You win!')
elif player == computer:
    print('😊Tie game!')
else:
    print('🐍 Python win!')
```

- Kiểm tra tất cả các trường hợp thắng/thua/hòa

## Luật chơi

- 🪨 Rock (Búa) thắng ✂️ Scissors (Kéo)
- 📄 Paper (Bao) thắng 🪨 Rock (Búa)
- ✂️ Scissors (Kéo) thắng 📄 Paper (Bao)

## Cách chạy chương trình

```bash
python rps.py
```

## Kết quả mong đợi

```text
RPS.PAPER
RPS.ROCK
RPS.ROCK
1

Enter...
1 for Rock,
2 for Paper, or
3 for Scissors:

2

You chose PAPER.
Python chose ROCK.

🎉You win!
```
