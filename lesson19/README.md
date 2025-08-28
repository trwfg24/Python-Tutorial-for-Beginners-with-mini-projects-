# Bài 19: Xử Lý Ngoại Lệ (Exception Handling) trong Python

## Tổng Quan

Bài học này bao gồm việc xử lý ngoại lệ trong Python, đây là một khái niệm lập trình quan trọng cho phép bạn xử lý lỗi một cách uyển chuyển và ngăn chương trình bị crash bất ngờ.

## Những Gì Bạn Sẽ Học

- Hiểu về ngoại lệ và xử lý lỗi
- Sử dụng khối try-except
- Xử lý các loại ngoại lệ cụ thể
- Tạo ngoại lệ tùy chỉnh
- Sử dụng mệnh đề else và finally
- Thực hành tốt nhất cho xử lý ngoại lệ

## Các Khái Niệm Chính

### 1. Ngoại Lệ Là Gì?

Ngoại lệ là các sự kiện xảy ra trong quá trình thực thi chương trình làm gián đoạn luồng bình thường của các lệnh. Python có nhiều loại ngoại lệ tích hợp như:

- `NameError`: Được raise khi một biến không được định nghĩa
- `ZeroDivisionError`: Được raise khi chia cho zero
- `TypeError`: Được raise khi thực hiện phép toán trên kiểu dữ liệu không phù hợp
- `ValueError`: Được raise khi hàm nhận đối số có kiểu đúng nhưng giá trị không phù hợp

### 2. Cấu Trúc Try-Except

```python
try:
    # Code có thể gây ra ngoại lệ
    risky_code()
except ExceptionType:
    # Code để xử lý ngoại lệ
    handle_error()
```

### 3. Xử Lý Nhiều Ngoại Lệ

Bạn có thể xử lý các loại ngoại lệ khác nhau riêng biệt:

```python
try:
    # code nguy hiểm
except NameError:
    # xử lý NameError
except ZeroDivisionError:
    # xử lý ZeroDivisionError
except Exception as error:
    # xử lý tất cả các ngoại lệ khác
```

### 4. Ngoại Lệ Tùy Chỉnh

Bạn có thể tạo các lớp ngoại lệ riêng bằng cách kế thừa từ lớp `Exception`:

```python
class CustomError(Exception):
    pass
```

### 5. Mệnh Đề Else và Finally

- **else**: Chỉ chạy nếu không có ngoại lệ nào được raise trong khối try
- **finally**: Luôn chạy, bất kể có ngoại lệ xảy ra hay không

## Giải Thích Ví Dụ Code

File `exceptions.py` minh họa:

1. **Tạo Ngoại Lệ Tùy Chỉnh**: Lớp `JustNotCoolError` cho thấy cách tạo ngoại lệ tùy chỉnh
2. **Khối Try**: Chứa code có thể gây ra ngoại lệ
3. **Nhiều Khối Except**: Xử lý các loại ngoại lệ khác nhau
4. **Bắt Đối Tượng Ngoại Lệ**: Sử dụng `as error` để bắt chi tiết ngoại lệ
5. **Mệnh Đề Else**: Thực thi khi không có ngoại lệ nào xảy ra
6. **Mệnh Đề Finally**: Luôn thực thi để dọn dẹp code

## Chạy Code

Để chạy ví dụ:

```bash
python exceptions.py
```

Kết quả mong đợi:

```text
An exception occurred: This just isn't cool, man.
I'm going to print with or without an error.
```

## Thực Hành Tốt Nhất

1. **Cụ Thể**: Bắt các ngoại lệ cụ thể thay vì sử dụng câu lệnh `except:` rộng
2. **Ghi Log Lỗi**: Luôn ghi log hoặc xử lý ngoại lệ một cách phù hợp
3. **Dọn Dẹp**: Sử dụng khối `finally` cho các thao tác dọn dẹp
4. **Đừng Bỏ Qua**: Không bao giờ sử dụng khối except rỗng mà không xử lý lỗi
5. **Ngoại Lệ Tùy Chỉnh**: Tạo các ngoại lệ tùy chỉnh có ý nghĩa cho ứng dụng của bạn

## Các Loại Ngoại Lệ Phổ Biến

| Ngoại Lệ            | Mô Tả                      | Ví Dụ                        |
| ------------------- | -------------------------- | ---------------------------- |
| `NameError`         | Biến không được định nghĩa | Sử dụng biến chưa định nghĩa |
| `ZeroDivisionError` | Chia cho zero              | `5 / 0`                      |
| `TypeError`         | Sai kiểu dữ liệu           | `"hello" + 5`                |
| `ValueError`        | Sai giá trị cho kiểu đúng  | `int("hello")`               |
| `FileNotFoundError` | File không tồn tại         | Mở file không tồn tại        |
| `IndexError`        | Chỉ số list ngoài phạm vi  | `list[100]` cho list ngắn    |
