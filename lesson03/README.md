# Lesson 03: Conditional Statements và Ternary Operator

## Mục tiêu bài học

Trong bài học này, bạn sẽ học về:

- Câu lệnh điều kiện if/else
- Toán tử ternary (conditional expression)
- Cách viết code ngắn gọn hơn với ternary operator

## Nội dung chính

### 1. Câu lệnh điều kiện if/else

```python
if condition:
    # Code thực thi khi điều kiện đúng
else:
    # Code thực thi khi điều kiện sai
```

### 2. Ternary Operator (Toán tử ba ngôi)

Ternary operator cho phép viết câu lệnh if/else trên một dòng:

```python
# Cú pháp: value_if_true if condition else value_if_false
print('Right one!') if meaning > 10 else print('Not today!')
```

## Code trong bài học

File `meaning.py` minh họa:

- Khai báo biến `meaning = 15`
- Sử dụng ternary operator để kiểm tra điều kiện
- So sánh cách viết ngắn gọn với if/else truyền thống

## Cách chạy code

```bash
python meaning.py
```

## Kết quả mong đợi

Khi chạy file `meaning.py`, chương trình sẽ in ra:

- Một dòng trống (do `print()`)
- "Right one!" (vì meaning = 15 > 10)

## Bài tập thực hành

1. Thay đổi giá trị của biến `meaning` thành các giá trị khác nhau (< 10, = 10, > 10)
2. Thử viết các ternary operator khác với điều kiện khác nhau
3. So sánh hiệu suất và độ dễ đọc giữa if/else và ternary operator

## Ghi chú

- Ternary operator hữu ích khi cần gán giá trị dựa trên điều kiện đơn giản
- Không nên lạm dụng ternary operator với điều kiện phức tạp vì sẽ làm code khó đọc
- Trong file có phần code if/else được comment để so sánh
