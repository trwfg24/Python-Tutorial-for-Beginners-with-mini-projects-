# Bài 09: Hàm (Functions) trong Python

## Mục tiêu học tập

Trong bài học này, bạn sẽ học được:

- Cách định nghĩa và sử dụng hàm trong Python
- Tham số mặc định (Default parameters)
- Kiểm tra kiểu dữ liệu trong hàm
- Sử dụng \*args để nhận nhiều tham số
- Sử dụng \*\*kwargs để nhận tham số có tên

## Nội dung kiến thức

### 1. Định nghĩa hàm cơ bản

```python
def hello_world():
    print("Hello world!")

hello_world()
```

**Giải thích:**

- Từ khóa `def` được sử dụng để định nghĩa một hàm
- `hello_world()` là tên hàm
- Dấu `:` kết thúc dòng định nghĩa hàm
- Nội dung hàm được viết với thụt lề (indentation)
- Gọi hàm bằng cách sử dụng tên hàm và dấu ngoặc đơn

### 2. Hàm với tham số và giá trị trả về

```python
def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2
```

**Các khái niệm quan trọng:**

- **Tham số mặc định (Default parameters)**: `num1=0, num2=0` - nếu không truyền giá trị, sẽ sử dụng giá trị mặc định
- **Kiểm tra kiểu dữ liệu**: `type(num1) is not int` - đảm bảo tham số là số nguyên
- **Giá trị trả về**: `return` trả về kết quả từ hàm
- **Xử lý lỗi**: Trả về 0 nếu tham số không phải là số nguyên

### 3. Sử dụng \*args (Arguments)

```python
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")
```

**Giải thích:**

- `*args` cho phép hàm nhận nhiều tham số không xác định trước
- Các tham số được lưu trữ dưới dạng tuple
- Có thể truyền bất kỳ số lượng tham số nào
- Hữu ích khi không biết trước số lượng tham số

### 4. Sử dụng \*\*kwargs (Keyword Arguments)

```python
def mul_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mul_named_items(first="Dave", last="John")
```

**Giải thích:**

- `**kwargs` cho phép hàm nhận các tham số có tên (key-value pairs)
- Các tham số được lưu trữ dưới dạng dictionary
- Tham số được truyền dưới dạng `key=value`
- Hữu ích khi muốn truyền dữ liệu có cấu trúc

## Kết quả chạy chương trình

Khi chạy file `functions.py`, bạn sẽ thấy kết quả:

```text
Hello world!
0
('Dave', 'John', 'Sara')
<class 'tuple'>
{'first': 'Dave', 'last': 'John'}
<class 'dict'>
```

## Ứng dụng thực tế

1. **Hàm cơ bản**: Dùng để thực hiện các tác vụ lặp lại
2. **Tham số mặc định**: Tạo hàm linh hoạt, có thể hoạt động với hoặc không có tham số
3. **Kiểm tra kiểu dữ liệu**: Đảm bảo hàm hoạt động đúng với dữ liệu đầu vào
4. **\*args**: Xử lý danh sách động các tham số
5. \***\*kwargs**: Xử lý cấu hình hoặc tùy chọn linh hoạt
