# Lesson 17: Lambda Functions - Hàm ẩn danh trong Python

## Giới thiệu

Bài học này tập trung vào **Lambda Functions** (hàm ẩn danh) - một tính năng mạnh mẽ của Python cho phép tạo các hàm ngắn gọn, không cần khai báo `def`. Lambda thường được sử dụng với các hàm built-in như `map()`, `filter()`, và `reduce()` để xử lý dữ liệu một cách hiệu quả.

---

## Phân tích chi tiết code và kiến thức sử dụng

### 1. Lambda Functions cơ bản

```python
squared = lambda num: num * num
addTwo = lambda num: num + 2
sum = lambda a, b: a + b
```

#### Kiến thức chính

- **Cú pháp Lambda:** `lambda tham_số: biểu_thức`
- **So sánh với hàm thường:**

  ```python
  # Lambda
  squared = lambda num: num * num

  # Tương đương với hàm thường
  def squared(num):
      return num * num
  ```

- **Đặc điểm:**
  - Chỉ có thể chứa 1 biểu thức duy nhất
  - Tự động return kết quả của biểu thức
  - Không cần từ khóa `return`
  - Thường dùng cho logic đơn giản

### 2. Lambda với Closure - Hàm tạo hàm

```python
def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
```

#### Kiến thức về Closure

- **Closure pattern:** Hàm `funcBuilder` trả về lambda có quyền truy cập biến `x`
- **Lexical scoping:** Lambda "nhớ" giá trị `x` từ scope ngoài
- **Factory function:** Tạo nhiều hàm khác nhau từ cùng 1 template
- **Ứng dụng thực tế:** Tạo validator, converter, calculator functions

### 3. Lambda với map() - Biến đổi dữ liệu

```python
numbers = [3, 7, 8, 12, 18, 21]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))  # [9, 49, 64, 144, 324, 441]
```

#### Kiến thức về map()

- **map() function:** Áp dụng hàm lên từng phần tử của iterable
- **Cú pháp:** `map(function, iterable)`
- **Return type:** Map object (iterator) - cần convert sang `list()` để in
- **Functional programming:** Xử lý dữ liệu theo paradigm functional
- **Tương đương với list comprehension:** `[num * num for num in numbers]`

### 4. Lambda với filter() - Lọc dữ liệu

```python
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))  # [3, 7, 21]
```

#### Kiến thức về filter()

- **filter() function:** Lọc các phần tử thỏa mãn điều kiện
- **Điều kiện:** Lambda phải return `True`/`False`
- **Return type:** Filter object (iterator)
- **Logic filtering:** `num % 2 != 0` kiểm tra số lẻ
- **Tương đương với list comprehension:** `[num for num in numbers if num % 2 != 0]`

### 5. Lambda với reduce() - Tích lũy dữ liệu

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)  # 16

names = ["Dave Gray", "Sara Ito", "John Jacob"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)  # 24
```

#### Kiến thức về reduce()

- **reduce() function:** Tích lũy giá trị từ iterable thành 1 giá trị duy nhất
- **Import:** Phải import từ `functools` module
- **Cú pháp:** `reduce(function, iterable, initial_value)`
- **Accumulator pattern:**
  - `acc` (accumulator): giá trị tích lũy
  - `curr` (current): phần tử hiện tại
- **Initial value:** Giá trị khởi tạo cho accumulator (optional)
- **Ứng dụng:** Tính tổng, tìm max/min, ghép chuỗi, đếm

---

## So sánh Lambda vs Hàm thường

| Tiêu chí  | Lambda                   | Hàm thường                  |
| --------- | ------------------------ | --------------------------- |
| Cú pháp   | `lambda x: x*2`          | `def func(x): return x*2`   |
| Độ dài    | 1 dòng, 1 biểu thức      | Nhiều dòng, nhiều statement |
| Tên       | Ẩn danh                  | Có tên                      |
| Scope     | Local, thường dùng 1 lần | Global, tái sử dụng         |
| Debugging | Khó debug                | Dễ debug                    |
| Ứng dụng  | map, filter, reduce      | Logic phức tạp              |

---

## Luồng hoạt động của chương trình

1. **Khai báo Lambda cơ bản:** Tạo các hàm đơn giản cho phép toán
2. **Closure với Lambda:** Sử dụng factory function để tạo lambda động
3. **map() processing:** Biến đổi mỗi phần tử trong list
4. **filter() processing:** Lọc phần tử theo điều kiện
5. **reduce() processing:** Tích lũy tất cả phần tử thành 1 giá trị

---

## Khi nào nên sử dụng Lambda?

### ✅ Nên dùng Lambda

- Logic đơn giản, 1 dòng
- Dùng với `map()`, `filter()`, `reduce()`
- Callback functions
- Event handling
- Sorting với custom key: `sorted(data, key=lambda x: x[1])`

### ❌ Không nên dùng Lambda

- Logic phức tạp, nhiều dòng
- Cần tái sử dụng nhiều lần
- Cần docstring và documentation
- Debugging phức tạp

---

## Tổng kết kiến thức đã sử dụng

- **Lambda Functions:** Hàm ẩn danh ngắn gọn
- **Closure:** Lambda truy cập biến từ scope ngoài
- **map():** Biến đổi từng phần tử của iterable
- **filter():** Lọc phần tử theo điều kiện boolean
- **reduce():** Tích lũy iterable thành 1 giá trị
- **functools module:** Import reduce function
- **Iterator pattern:** map, filter, reduce đều trả về iterator
- **Functional programming:** Paradigm lập trình hàm

---
