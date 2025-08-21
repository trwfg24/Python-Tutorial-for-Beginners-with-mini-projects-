# Bài 14: Modules (Modules và Packages)

## Tổng quan

Bài học này giới thiệu về **Modules** trong Python - một tính năng quan trọng giúp tổ chức và tái sử dụng code một cách hiệu quả.

## Nội dung chính

### 1. Import Modules

- **Import toàn bộ module**: `import math`, `import sys`
- **Import với alias**: `import random as rdm`
- **Import từ module cụ thể**: `from math import pi`
- **Import từ enum**: `from enum import Enum`

### 2. Sử dụng Built-in Modules

- **math module**: Sử dụng `pi` từ module math
- **sys module**: Quản lý hệ thống Python
- **random module**: Tạo số ngẫu nhiên với alias `rdm`
- **enum module**: Tạo enumeration

### 3. Tạo Custom Module

- **kansas.py**: Module tự tạo chứa:
  - Các biến: `capital`, `bird`, `flower`, `song`
  - Hàm `randomfunfact()`: Hiển thị thông tin ngẫu nhiên về Kansas
  - Sử dụng `if __name__ == "__main__":` để kiểm tra module được chạy trực tiếp

### 4. Import và Sử dụng Custom Module

- Import module `kansas`: `import kansas`
- Truy cập biến: `kansas.capital`
- Gọi hàm: `kansas.randomfunfact()`
- Import hàm từ module khác: `from rps7 import rock_paper_scissors`

### 5. Kiểm tra Tên Module

- `__name__`: Tên của module hiện tại
- `kansas.__name__`: Tên của module kansas
- Hiểu được sự khác biệt khi module được import vs chạy trực tiếp

## Các file trong bài học

### modules.py

File chính demonstrating cách import và sử dụng các modules khác nhau.

### kansas.py

Module tự tạo chứa thông tin về bang Kansas, bao gồm:

- Thông tin cơ bản (thủ phủ, chim, hoa, bài hát)
- Hàm tạo thông tin ngẫu nhiên thú vị
- Demonstration của `if __name__ == "__main__"`

### rps7.py

Module game "Rock Paper Scissors" được import và sử dụng trong modules.py.

## Kiến thức đạt được

- Hiểu cách import modules trong Python
- Biết cách tạo và sử dụng custom modules
- Sử dụng alias khi import
- Hiểu về `__name__` và `if __name__ == "__main__"`
- Tổ chức code thành các modules để tái sử dụng
- Sử dụng các built-in modules phổ biến

## Lưu ý quan trọng

- Modules giúp tổ chức code tốt hơn và tránh lặp lại
- Sử dụng `if __name__ == "__main__":` để code chỉ chạy khi file được execute trực tiếp
- Import chỉ những gì cần thiết để tối ưu performance
- Đặt tên modules và biến rõ ràng, dễ hiểu
