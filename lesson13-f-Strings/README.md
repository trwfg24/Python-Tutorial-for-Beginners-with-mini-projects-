# Bài 13: F-Strings và String Formatting trong Python

## Mục tiêu học tập

Trong bài học này, bạn sẽ học về:

- Hiểu các phương pháp định dạng chuỗi trong Python
- Sử dụng f-strings (formatted string literals) - cách tốt nhất
- So sánh các phương pháp: concatenation, % formatting, .format(), f-strings
- Định dạng số, phần trăm và độ chính xác thập phân
- Áp dụng f-strings trong dự án game Rock-Paper-Scissors với closures

## Nội dung chi tiết

### 1. Các phương pháp định dạng chuỗi

Python cung cấp nhiều cách để định dạng và kết hợp chuỗi:

#### 1.1 String Concatenation (Nối chuỗi)

```python
person = "Dave"
coins = 3
message = person + " has " + str(coins) + " coins left."
```

**Nhược điểm:**

- Phải chuyển đổi kiểu dữ liệu (str())
- Khó đọc khi có nhiều biến
- Hiệu suất thấp với chuỗi dài

#### 1.2 % Formatting (Old style)

```python
message = "%s has %s coins left." % (person, coins)
```

**Đặc điểm:**

- Cú pháp cũ, tương tự C/printf
- `%s` cho string, `%d` cho integer, `%f` cho float

#### 1.3 .format() Method

```python
# Cơ bản
message = "{} has {} coins left.".format(person, coins)

# Với chỉ số
message = "{1} has {0} coins left.".format(coins, person)

# Với tên tham số
message = "{person} has {coins} coins left.".format(person=person, coins=coins)

# Với dictionary unpacking
player = {"person": "Dave", "coins": 3}
message = "{person} has {coins} coins left.".format(**player)
```

### 2. F-Strings - Phương pháp tốt nhất

**F-strings** (formatted string literals) được giới thiệu từ Python 3.6:

#### 2.1 Cú pháp cơ bản:

```python
message = f"{person} has {coins} coins left."
```

#### 2.2 Biểu thức trong f-strings:

```python
message = f"{person} has {2 * 5} coins left."
message = f"{person.lower()} has {2 * 5} coins left."
message = f"{player['person']} has {2 * 5} coins left."
```

#### 2.3 Định dạng số:

```python
num = 10
print(f"2.25 times {num} is {2.25 * num:.2f}")  # 2 chữ số thập phân
```

#### 2.4 Định dạng phần trăm:

```python
for num in range(1, 11):
    print(f"{num} divided by 4.25 is {num / 4.25:.2%}")  # Phần trăm với 2 chữ số
```

### 3. Format Specifiers (Bộ định dạng)

#### Cú pháp: `{value:format_spec}`

| Format | Mô tả                            | Ví dụ                       |
| ------ | -------------------------------- | --------------------------- |
| `:.2f` | Float với 2 chữ số thập phân     | `{3.14159:.2f}` → `3.14`    |
| `:.2%` | Phần trăm với 2 chữ số thập phân | `{0.1234:.2%}` → `12.34%`   |
| `:,`   | Ngăn cách hàng nghìn             | `{1234567:,}` → `1,234,567` |
| `:>10` | Căn phải trong 10 ký tự          | `{42:>10}` → `        42`   |
| `:<10` | Căn trái trong 10 ký tự          | `{42:<10}` → `42        `   |
| `:^10` | Căn giữa trong 10 ký tự          | `{42:^10}` → `  42  `       |

## Files trong bài học

### `f_strings.py`

File demo tất cả các phương pháp định dạng chuỗi:

**Nội dung chính:**

- So sánh 4 phương pháp định dạng chuỗi
- Demo f-strings với biểu thức
- Định dạng số với độ chính xác
- Vòng lặp với f-strings formatting

**Progression từ cũ đến mới:**

1. String concatenation → Khó đọc
2. % formatting → Cú pháp cũ
3. .format() → Linh hoạt nhưng dài dòng
4. **f-strings** → Ngắn gọn, dễ đọc, hiệu suất cao

### `rps6.py`

Phiên bản Rock-Paper-Scissors kết hợp f-strings và closures:

**Tính năng mới:**

- **F-strings** cho tất cả output formatting
- **Closures** để quản lý game state
- **Nonlocal** variables cho player_wins, python_wins
- **Nested functions** với decide_winner() bên trong play_rps()
- **Game statistics** hiển thị bằng f-strings

**Cải tiến về formatting:**

```python
# Hiển thị lựa chọn
print(f"\nYou chose {str(RPS(player)).replace('RPS.', '')}.")
print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

# Hiển thị thống kê
print(f"\nGame count: {str(game_count)}")
print(f"\nPlayer wins: {str(player_wins)}")
print(f"\nPython wins: {str(python_wins)}")
```

**Kiến trúc code:**

- **Closure pattern**: `rps()` trả về `play_rps()`
- **State management**: game_count, player_wins, python_wins
- **Nested function**: decide_winner() với nonlocal access
- **Clean formatting**: f-strings cho tất cả output

## So sánh các phương pháp

| Phương pháp       | Ưu điểm                 | Nhược điểm          | Khuyến nghị              |
| ----------------- | ----------------------- | ------------------- | ------------------------ |
| **Concatenation** | Đơn giản                | Khó đọc, cần str()  | ❌ Tránh                 |
| **% formatting**  | Quen thuộc (C-style)    | Cú pháp cũ, hạn chế | ❌ Legacy code only      |
| **.format()**     | Linh hoạt, mạnh mẽ      | Dài dòng            | ⚠️ OK nhưng không tối ưu |
| **F-strings**     | Ngắn gọn, nhanh, dễ đọc | Cần Python 3.6+     | ✅ **Khuyến nghị**       |

## Best Practices

### 1. Sử dụng F-strings

```python
# ✅ Tốt
name = "Alice"
age = 25
message = f"Hello {name}, you are {age} years old."

# ❌ Tránh
message = "Hello " + name + ", you are " + str(age) + " years old."
```

### 2. Định dạng số

```python
# ✅ Tốt
price = 19.99
print(f"Price: ${price:.2f}")  # Price: $19.99

# ✅ Phần trăm
rate = 0.1234
print(f"Rate: {rate:.1%}")     # Rate: 12.3%
```

### 3. Alignment và Padding

```python
# ✅ Căn chỉnh
items = [("Apple", 1.99), ("Banana", 0.59)]
for item, price in items:
    print(f"{item:<10} ${price:>6.2f}")
```

### 4. Debug với f-strings

```python
# ✅ Debug nhanh (Python 3.8+)
value = 42
print(f"{value=}")  # value=42
```

## Hiệu suất

**Thứ tự hiệu suất (nhanh → chậm):**

1. **F-strings** - Nhanh nhất
2. .format() - Trung bình
3. % formatting - Chậm hơn
4. Concatenation - Chậm nhất với nhiều biến

## Lưu ý quan trọng

### 1. Python Version

- **F-strings** cần Python 3.6+
- **Debug f-strings** (`{var=}`) cần Python 3.8+

### 2. Security

```python
# ⚠️ Cẩn thận với user input
user_input = "malicious_code"
# Không bao giờ làm: eval(f"print({user_input})")
```

### 3. Performance

- F-strings được compile-time optimized
- Nhanh hơn .format() và % formatting
- Tốt nhất cho string với ít biến

## Thuật ngữ quan trọng

- **String formatting**: Định dạng chuỗi
- **F-strings/f-literals**: Formatted string literals
- **Format specifier**: Bộ định dạng (.2f, .2%, etc.)
- **String interpolation**: Nội suy chuỗi
- **Concatenation**: Nối chuỗi
- **Padding**: Đệm ký tự
- **Alignment**: Căn chỉnh (left, right, center)
- **Precision**: Độ chính xác (cho số thập phân)

## Examples nâng cao

### Multi-line f-strings:

```python
name = "Alice"
age = 30
message = (
    f"Hello {name}!\n"
    f"You are {age} years old.\n"
    f"Next year you'll be {age + 1}."
)
```

### F-strings với functions:

```python
def get_grade(score):
    return "A" if score >= 90 else "B"

score = 95
print(f"Score: {score}, Grade: {get_grade(score)}")
```

### Dictionary formatting:

```python
student = {"name": "Bob", "grade": 85}
print(f"Student: {student['name']}, Grade: {student['grade']}")
```
