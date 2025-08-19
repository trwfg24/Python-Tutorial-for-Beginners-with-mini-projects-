# Bài 01: Hello World - Chương trình Python đầu tiên của bạn

## Tổng quan

Bài học này giới thiệu bạn với lập trình Python thông qua chương trình kinh điển "Hello World". Bạn sẽ học các kiến thức cơ bản về cú pháp Python và cách chạy script Python đầu tiên.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ:

- Hiểu Python là gì và cách viết code Python cơ bản
- Học cách tạo và lưu trữ dữ liệu trong biến
- Sử dụng hàm `print()` để hiển thị kết quả
- Chạy chương trình Python đầu tiên của bạn

## Các file trong bài học này

- `hello.py` - Chương trình Python đầu tiên hiển thị "Hello World!"
- `README.md` - File tài liệu này

## Giải thích code

### hello.py

```python
greeting = 'Hello World!'
print(greeting)
```

**Code này làm gì:**

1. **Gán biến**: `greeting = 'Hello World!'`

   - Tạo một biến có tên `greeting`
   - Lưu trữ văn bản "Hello World!" trong biến này
   - Văn bản được đặt trong dấu nháy đơn, tạo thành một chuỗi (string)

2. **Hàm Print**: `print(greeting)`
   - Hiển thị nội dung của biến `greeting`
   - Hàm `print()` xuất văn bản ra console

## Khái niệm chính

### Biến (Variables)

- Biến là container để lưu trữ giá trị dữ liệu
- Trong Python, bạn không cần khai báo kiểu của biến
- Tên biến nên có ý nghĩa và tuân theo quy ước đặt tên Python

### Chuỗi (Strings)

- Chuỗi là dãy các ký tự được đặt trong dấu nháy
- Bạn có thể sử dụng dấu nháy đơn (`'`) hoặc dấu nháy kép (`"`)
- Ví dụ: `'Hello World!'` hoặc `"Hello World!"`

### Hàm print()

- Hàm có sẵn trong Python để hiển thị kết quả
- Có thể in biến, chuỗi, số và nhiều thứ khác
- Cú pháp: `print(giá_trị_cần_hiển_thị)`

## Cách chạy chương trình này

1. **Sử dụng Command Line:**

   ```bash
   python hello.py
   ```

2. **Sử dụng VS Code:**

   - Mở `hello.py` trong VS Code
   - Nhấn `Ctrl + F5` để chạy không debug
   - Hoặc nhấn `F5` để chạy có debug

3. **Kết quả mong đợi:**
   ```
   Hello World!
   ```

## Bài tập thực hành

1. **Sửa lời chào:**

   - Thay đổi "Hello World!" thành tên của bạn
   - Ví dụ: `greeting = 'Xin chào Lan!'`

2. **Thêm nhiều biến:**

   ```python
   name = 'Tên của bạn'
   message = 'Chào mừng đến với Python!'
   print(name)
   print(message)
   ```

3. **Nối chuỗi:**
   ```python
   first_name = 'Nguyễn'
   last_name = 'Văn A'
   full_name = first_name + ' ' + last_name
   print(full_name)
   ```

## Lỗi thường gặp cần tránh

1. **Quên dấu nháy quanh chuỗi:**

   - ❌ `greeting = Hello World!`
   - ✅ `greeting = 'Hello World!'`

2. **Dấu nháy không khớp:**

   - ❌ `greeting = 'Hello World!"`
   - ✅ `greeting = 'Hello World!'`

3. **Phân biệt chữ hoa chữ thường:**
   - Python phân biệt chữ hoa chữ thường
   - `print` khác với `Print`

## Bước tiếp theo

Tiếp tục với Bài 02 để học thêm về các kiến thức cơ bản Python và tương tác với người dùng!

## Có câu hỏi?

Nếu bạn có bất kỳ câu hỏi nào về bài học này, hãy xem lại code và thử các bài tập. Lập trình học tốt nhất là thông qua thực hành!
