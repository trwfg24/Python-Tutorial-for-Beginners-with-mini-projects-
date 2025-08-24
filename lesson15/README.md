# Lesson 15: Command Line Arguments và phân tích code Python thực tế

## Giới thiệu

Bài học này giúp bạn hiểu rõ cách sử dụng các kiến thức Python nền tảng thông qua hai ví dụ thực tế: chương trình chào người dùng (`hello_person.py`) và trò chơi kéo-búa-bao (`rps8.py`).

---

## 1. hello_person.py

### Chức năng

Chào người dùng bằng tên và ngôn ngữ được chọn qua tham số dòng lệnh.

### Phân tích chi tiết code và kiến thức sử dụng

#### Giải thích về parser.add_argument('-n', '--name', ...)

```python
parser.add_argument(
  "-n",
  "--name",
  metavar="name",
  required=True,
  help="The name of the person to greet."
)
```

- `-n` và `--name`: Định nghĩa hai cách nhập tham số trên dòng lệnh, có thể dùng ngắn gọn `-n` hoặc đầy đủ `--name`.
- `metavar="name"`: Khi hiển thị hướng dẫn sử dụng, sẽ hiện từ "name" để người dùng biết cần nhập gì.
- `required=True`: Tham số này bắt buộc phải có khi chạy chương trình, nếu thiếu sẽ báo lỗi.
- `help=...`: Chuỗi mô tả, sẽ hiển thị khi dùng lệnh `--help` để hướng dẫn người dùng.

Như vậy, dòng này giúp chương trình nhận tên người dùng từ command line một cách rõ ràng, chuyên nghiệp và thân thiện.

- **Hàm (Function):** Định nghĩa hàm `hello(name, lang)` để xử lý logic chào người dùng. Hàm giúp đóng gói logic, tái sử dụng và làm code gọn gàng.

- **Dictionary (Từ điển):** Sử dụng dictionary `greetings` để ánh xạ ngôn ngữ sang lời chào. Dictionary là cấu trúc dữ liệu cho phép truy xuất giá trị theo key, rất tiện lợi khi cần tra cứu nhanh.

- **F-string:** Dùng f-string để định dạng chuỗi: `f"{greetings[lang]} {name}"`. F-string giúp chèn biến vào chuỗi một cách trực quan, dễ đọc.

- **argparse (Xử lý tham số dòng lệnh):** Sử dụng module `argparse` để định nghĩa và lấy tham số `-n/--name` (tên) và `-l/--lang` (ngôn ngữ). Argparse giúp chương trình nhận dữ liệu từ ngoài, kiểm tra hợp lệ, sinh hướng dẫn tự động.

- **Idioms:** Sử dụng `if __name__ == "__main__":` để đảm bảo code chỉ chạy khi file được thực thi trực tiếp, không chạy khi import từ file khác.

#### Luồng hoạt động cụ thể

1. Người dùng nhập tên và ngôn ngữ qua dòng lệnh.

2. Argparse kiểm tra và lấy giá trị các tham số.

3. Gọi hàm `hello(name, lang)` để in lời chào phù hợp.

4. Nếu nhập sai ngôn ngữ, chương trình báo lỗi và hướng dẫn lại.

#### Ví dụ dòng lệnh

```bash
python hello_person.py -n "Truong" -l "English"
```

---

## 2. rps8.py

### Chức năng

Trò chơi kéo-búa-bao, nhập tên người chơi từ dòng lệnh, chơi nhiều ván, thống kê kết quả.

### Phân tích chi tiết code và kiến thức sử dụng

- **Hàm lồng nhau (Nested Function):** Định nghĩa hàm `play_rps()` bên trong hàm `rps(name)` để quản lý logic từng ván chơi. Hàm lồng nhau giúp cô lập logic, chỉ dùng trong phạm vi cần thiết.

- **Enum:** Sử dụng `Enum` để định nghĩa các lựa chọn ROCK, PAPER, SCISSORS. Enum giúp code rõ ràng, tránh nhầm lẫn giữa các giá trị số.

- **Biến nonlocal:** Dùng từ khóa `nonlocal` để cập nhật biến đếm số ván/thắng ở phạm vi ngoài hàm lồng nhau. Nonlocal cho phép thay đổi biến ở scope cha gần nhất, rất hữu ích khi cần cập nhật trạng thái trong hàm lồng nhau.

- **Vòng lặp và điều kiện:** Sử dụng vòng lặp để cho phép chơi nhiều ván, kiểm tra nhập liệu hợp lệ, hỏi người chơi có tiếp tục không. Điều kiện giúp kiểm soát luồng chương trình, xử lý các trường hợp khác nhau.

- **argparse:** Nhận tên người chơi từ dòng lệnh với tham số `-n/--name`. Giúp chương trình linh hoạt, dễ mở rộng.

- **F-string:** Định dạng chuỗi khi in kết quả từng ván, tổng kết số ván thắng/thua, giúp thông báo rõ ràng, sinh động.

#### Luồng hoạt động cụ thể

1. Nhận tên người chơi từ dòng lệnh bằng argparse.

2. Bắt đầu vòng lặp trò chơi:

   - Hỏi lựa chọn của người chơi (1: Kéo, 2: Búa, 3: Bao).
   - Máy chọn ngẫu nhiên một lựa chọn.
   - So sánh kết quả, xác định thắng/thua/hòa.
   - Cập nhật biến đếm số ván, số lần thắng của mỗi bên.
   - In kết quả từng ván, tổng kết số ván thắng/thua.
   - Hỏi người chơi có muốn tiếp tục không (Y: tiếp tục, Q: thoát).

3. Nếu người chơi chọn thoát, in lời cảm ơn và kết thúc chương trình.

#### Ví dụ dòng lệnh

```bash
python rps8.py -n "Truong"
```

---

## 3. Tổng kết kiến thức đã sử dụng

- Hàm, hàm lồng nhau (nested function)
- Dictionary (từ điển)
- Enum
- F-string
- Vòng lặp, điều kiện, kiểm tra nhập liệu
- Biến nonlocal
- Xử lý tham số dòng lệnh với argparse
- Idioms Python (`if __name__ == "__main__":`)

---

**Hãy đọc kỹ từng file code, đối chiếu với giải thích trên để hiểu sâu hơn về cách tổ chức và vận dụng kiến thức Python vào thực tế!**

# Bài học 15: Phân tích chi tiết code và kiến thức Python đã sử dụng

## Giới thiệu

Bài học này giúp bạn hiểu rõ cách sử dụng các kiến thức Python nền tảng thông qua hai ví dụ thực tế: chương trình chào người dùng (`hello_person.py`) và trò chơi kéo-búa-bao (`rps8.py`).

---

## 1. hello_person.py

### Chức năng

Chào người dùng bằng tên và ngôn ngữ được chọn qua tham số dòng lệnh.

### Phân tích chi tiết code và kiến thức sử dụng

- **Hàm (Function):**

  - Định nghĩa hàm `hello(name, lang)` để xử lý logic chào người dùng.

- **Dictionary (Từ điển):**

  - Sử dụng dictionary `greetings` để ánh xạ ngôn ngữ sang lời chào.

- **F-string:**

  - Dùng f-string để định dạng chuỗi: `f"{greetings[lang]} {name}"`.

- **argparse (Xử lý tham số dòng lệnh):**

  - Sử dụng module `argparse` để định nghĩa và lấy tham số `-n/--name` (tên) và `-l/--lang` (ngôn ngữ).
  - Kiểm tra giá trị hợp lệ cho ngôn ngữ.

- **Idioms:**
  - Sử dụng `if __name__ == "__main__":` để đảm bảo code chỉ chạy khi file được thực thi trực tiếp.

### Luồng hoạt động

1. Người dùng nhập tên và ngôn ngữ qua dòng lệnh.
2. Chương trình kiểm tra hợp lệ, gọi hàm `hello` để in lời chào phù hợp.

---

## 2. rps8.py

### Chức năng

Trò chơi kéo-búa-bao, nhập tên người chơi từ dòng lệnh, chơi nhiều ván, thống kê kết quả.

### Phân tích chi tiết code và kiến thức sử dụng

- **Hàm lồng nhau (Nested Function):**

  - Định nghĩa hàm `play_rps()` bên trong hàm `rps(name)` để quản lý logic từng ván chơi.

- **Enum:**

  - Sử dụng `Enum` để định nghĩa các lựa chọn ROCK, PAPER, SCISSORS giúp code rõ ràng, tránh nhầm lẫn số.

- **Biến nonlocal:**

  - Dùng từ khóa `nonlocal` để cập nhật biến đếm số ván/thắng ở phạm vi ngoài hàm lồng nhau.

- **Vòng lặp và điều kiện:**

  - Sử dụng vòng lặp để cho phép chơi nhiều ván, kiểm tra nhập liệu hợp lệ, hỏi người chơi có tiếp tục không.

- **argparse:**

  - Nhận tên người chơi từ dòng lệnh với tham số `-n/--name`.

- **F-string:**
  - Định dạng chuỗi khi in kết quả từng ván, tổng kết số ván thắng/thua.

### Luồng hoạt động

1. Nhận tên người chơi từ dòng lệnh.
2. Lặp lại: hỏi lựa chọn, máy chọn ngẫu nhiên, so sánh kết quả, in ra thắng/thua/hòa, thống kê.
3. Hỏi người chơi có muốn tiếp tục không.

---

## 3. Tổng kết kiến thức đã sử dụng

- Hàm, hàm lồng nhau
- Dictionary
- Enum
- F-string
- Vòng lặp, điều kiện, kiểm tra nhập liệu
- Biến nonlocal
- Xử lý tham số dòng lệnh với argparse
- Idioms Python (`if __name__ == "__main__":`)

---
