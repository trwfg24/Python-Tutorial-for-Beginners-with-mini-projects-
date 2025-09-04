# Bài 20: Lập trình hướng đối tượng (OOP) - Dự án tài khoản ngân hàng

## Mục tiêu học tập

Trong bài học này, bạn sẽ học:

- Khái niệm cơ bản về lập trình hướng đối tượng (OOP)
- Cách tạo và sử dụng class trong Python
- Kế thừa (Inheritance) trong Python
- Xử lý ngoại lệ (Exception Handling)
- Xây dựng một dự án thực tế: Hệ thống quản lý tài khoản ngân hàng

## Nội dung bài học

### 1. Tệp `bank_accounts.py`

Tệp này chứa các class chính của hệ thống:

#### Class `BalanceException`

- Là một ngoại lệ tùy chỉnh (custom exception)
- Được sử dụng khi số dư tài khoản không đủ để thực hiện giao dịch

#### Class `BankAccount` (Lớp cơ sở)

**Thuộc tính:**

- `balance`: Số dư tài khoản
- `name`: Tên chủ tài khoản

**Phương thức:**

- `__init__(self, initialAmount, acctName)`: Khởi tạo tài khoản với số tiền ban đầu và tên
- `getBalance()`: Hiển thị số dư hiện tại
- `deposit(amount)`: Gửi tiền vào tài khoản
- `withdraw(amount)`: Rút tiền từ tài khoản
- `transfer(amount, account)`: Chuyển tiền sang tài khoản khác
- `virableTransaction(amount)`: Kiểm tra tính khả thi của giao dịch

#### Class `InterestRewardsAcct` (Kế thừa từ BankAccount)

- Tài khoản có thưởng lãi suất
- Khi gửi tiền, sẽ được cộng thêm 5% (amount \* 1.05)

#### Class `SavingsAcct` (Kế thừa từ InterestRewardsAcct)

- Tài khoản tiết kiệm
- Có phí rút tiền: $5 cho mỗi lần rút
- Kế thừa tính năng thưởng lãi suất từ InterestRewardsAcct

### 2. Tệp `oop_project.py`

Tệp demo các tính năng của hệ thống:

**Các thao tác được thực hiện:**

1. Tạo tài khoản thường cho Dave và Sara
2. Kiểm tra số dư
3. Thực hiện gửi tiền
4. Thử rút tiền (bao gồm trường hợp rút quá số dư)
5. Chuyển tiền giữa các tài khoản
6. Tạo tài khoản có thưởng lãi suất (Jim)
7. Tạo tài khoản tiết kiệm (Blaze)

## Khái niệm OOP được sử dụng

### 1. Encapsulation (Đóng gói)

- Dữ liệu và phương thức được đóng gói trong class
- Kiểm soát quyền truy cập vào dữ liệu

### 2. Inheritance (Kế thừa)

```text
BankAccount (lớp cha)
    ↓
InterestRewardsAcct (lớp con)
    ↓
SavingsAcct (lớp cháu)
```

### 3. Polymorphism (Đa hình)

- Các lớp con override phương thức của lớp cha
- Ví dụ: `deposit()` và `withdraw()` được định nghĩa lại trong các lớp con

### 4. Exception Handling (Xử lý ngoại lệ)

- Sử dụng `try-except` để xử lý lỗi
- Tạo ngoại lệ tùy chỉnh `BalanceException`

## Cách chạy chương trình

1. Chạy tệp `oop_project.py`:

```bash
python oop_project.py
```

1. Hoặc import và sử dụng các class từ `bank_accounts.py`:

```python
from bank_accounts import *

# Tạo tài khoản mới
my_account = BankAccount(1000, "Tên của bạn")

# Thực hiện các giao dịch
my_account.deposit(500)
my_account.withdraw(200)
```

## Ghi chú quan trọng

- **Luôn kiểm tra số dư** trước khi thực hiện giao dịch
- **Sử dụng try-except** để xử lý các trường hợp lỗi
- **Kế thừa giúp tái sử dụng code** và mở rộng tính năng dễ dàng
- **Method overriding** cho phép tùy chỉnh hành vi của từng loại tài khoản

## Từ khóa Python được học

- `class`: Định nghĩa lớp
- `__init__`: Phương thức khởi tạo
- `super()`: Gọi phương thức của lớp cha
- `try/except`: Xử lý ngoại lệ
- `raise`: Ném ngoại lệ
- `self`: Tham chiếu đến đối tượng hiện tại
