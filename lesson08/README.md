# Lesson 08: Loops (Vòng lặp)

## Mục tiêu học tập

Trong bài học này, bạn sẽ học về:

- Vòng lặp `while`
- Vòng lặp `for`
- Các từ khóa điều khiển: `break`, `continue`
- Mệnh đề `else` trong vòng lặp
- Hàm `range()`
- Vòng lặp lồng nhau (nested loops)
- Ứng dụng thực tế: Game "Rock Paper Scissors" phiên bản 2

## 1. Vòng lặp While

Vòng lặp `while` thực hiện một khối lệnh cho đến khi điều kiện trở thành `False`.

```python
value = 1
while value <= 10:
    print(value)
    value += 1
```

### Sử dụng `break` trong while loop

```python
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break  # Thoát khỏi vòng lặp khi value = 5
    value += 1
```

### Sử dụng `continue` trong while loop

```python
value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue  # Bỏ qua phần còn lại, tiếp tục vòng lặp tiếp theo
    print(value)
```

### Mệnh đề `else` trong while loop

```python
while value <= 10:
    # khối lệnh
    value += 1
else:
    print('Value is now equal to ' + str(value))
    # Khối else được thực hiện khi điều kiện while = False
```

## 2. Vòng lặp For

Vòng lặp `for` được sử dụng để lặp qua các phần tử trong một chuỗi (list, string, tuple, etc.).

### Lặp qua danh sách

```python
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)
```

### Lặp qua chuỗi ký tự

```python
for x in 'Mississippi':
    print(x)  # In từng ký tự
```

### Sử dụng `break` trong for loop

```python
for x in names:
    if x == 'Sara':
        break  # Dừng khi gặp 'Sara'
    print(x)
```

### Sử dụng `continue` trong for loop

```python
for x in names:
    if x == 'Sara':
        continue  # Bỏ qua 'Sara', tiếp tục với phần tử tiếp theo
    print(x)
```

## 3. Hàm range()

Hàm `range()` tạo ra một chuỗi số để sử dụng trong vòng lặp for.

### range(stop)

```python
for x in range(4):
    print(x)  # In: 0, 1, 2, 3
```

### range(start, stop)

```python
for x in range(2, 4):
    print(x)  # In: 2, 3
```

### range(start, stop, step)

```python
for x in range(0, 100, 5):
    print(x)  # In: 0, 5, 10, 15, ..., 95
```

### Mệnh đề `else` trong for loop

```python
for x in range(0, 100, 5):
    print(x)
else:
    print("Glad that's over!")
    # Thực hiện sau khi vòng lặp hoàn thành
```

## 4. Vòng lặp lồng nhau (Nested Loops)

Bạn có thể đặt một vòng lặp bên trong vòng lặp khác.

```python
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for action in actions:
    for name in names:
        print(name + " " + action + ".")
```

## 5. Dự án thực hành: Rock Paper Scissors Game v2.0

File `rps2.py` là phiên bản cải tiến của game "Kéo Búa Bao" với các tính năng:

### Các tính năng chính:

- **Enum Class**: Sử dụng `RPS(Enum)` để định nghĩa các lựa chọn
- **Vòng lặp chơi lại**: Cho phép người chơi chơi nhiều lần
- **Xử lý lỗi đầu vào**: Kiểm tra input hợp lệ
- **Random choice**: Máy tính chọn ngẫu nhiên
- **Emoji**: Sử dụng emoji để làm game sinh động hơn

### Các kiến thức được áp dụng:

1. **Import modules**: `sys`, `random`, `enum`
2. **Class và Enum**: Định nghĩa class `RPS(Enum)`
3. **While loop**: Vòng lặp chính của game
4. **Input validation**: Kiểm tra input người dùng
5. **Conditional statements**: Logic xác định người thắng
6. **String manipulation**: Xử lý và format output
7. **Control flow**: `continue`, `break`, `sys.exit()`
