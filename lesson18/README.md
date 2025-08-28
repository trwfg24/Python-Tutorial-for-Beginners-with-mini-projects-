# Lesson 18: Classes (Lớp) trong Python

## Mục tiêu bài học

- Hiểu khái niệm Classes và Objects trong Python
- Học cách tạo và sử dụng classes
- Nắm vững các khái niệm OOP: Inheritance, Polymorphism
- Thực hành với constructor và methods

## Nội dung chính

### 1. Classes và Objects

- **Class**: Là một bản thiết kế (blueprint) để tạo ra objects
- **Object**: Là một instance (thể hiện) cụ thể của class
- **Attributes**: Các thuộc tính của object
- **Methods**: Các phương thức (hàm) của class

### 2. Constructor (**init**)

```python
def __init__(self, make, model):
    self.make = make
    self.model = model
```

- Phương thức đặc biệt được gọi khi tạo object mới
- `self` đại diện cho object hiện tại
- Dùng để khởi tạo các thuộc tính ban đầu

### 3. Inheritance (Kế thừa)

```python
class Airplane(Vehicle):  # Airplane kế thừa từ Vehicle
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # Gọi constructor của class cha
        self.faa_id = faa_id
```

- Cho phép class con kế thừa thuộc tính và phương thức từ class cha
- `super()` để truy cập methods của class cha
- Class con có thể thêm thuộc tính và phương thức riêng

### 4. Method Overriding

```python
def moves(self):
    print("Flies along..")  # Override phương thức moves() của class cha
```

- Class con có thể định nghĩa lại phương thức của class cha
- Tạo ra hành vi khác nhau cho từng loại object

### 5. Polymorphism (Đa hình)

```python
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()  # Cùng phương thức
    v.moves()          # Nhưng hành vi khác nhau
```

- Cùng một interface nhưng hành vi khác nhau
- Cho phép xử lý các object khác nhau theo cách thống nhất

## Cấu trúc code trong bài học

### Classes được định nghĩa:

1. **Vehicle** (Class cha):

   - Attributes: `make`, `model`
   - Methods: `moves()`, `get_make_model()`

2. **Airplane** (Kế thừa Vehicle):

   - Thêm attribute: `faa_id`
   - Override: `moves()` → "Flies along.."

3. **Truck** (Kế thừa Vehicle):

   - Override: `moves()` → "Rumbles along.."

4. **GolfCart** (Kế thừa Vehicle):
   - Không thay đổi gì (dùng `pass`)

### Objects được tạo:

- `my_car`, `your_car`: Vehicle objects
- `cessna`: Airplane object
- `mack`: Truck object
- `golfwagon`: GolfCart object

## Lưu ý quan trọng

### Best Practices:

1. Tên class nên viết hoa chữ cái đầu (PascalCase)
2. Tên method và attribute nên viết thường với dấu gạch dưới
3. Luôn nhớ gọi `super().__init__()` trong class con
4. Sử dụng `pass` khi class chưa có implementation

## Ứng dụng thực tế

- Quản lý các loại phương tiện giao thông
- Tạo hệ thống phân cấp objects
- Xây dựng game với nhiều loại nhân vật
- Quản lý nhân viên với các chức vụ khác nhau

## Từ khóa quan trọng

- `class`: Định nghĩa class
- `self`: Tham chiếu đến object hiện tại
- `__init__`: Constructor method
- `super()`: Truy cập class cha
- `pass`: Placeholder khi chưa có code
- Inheritance: Kế thừa
- Polymorphism: Đa hình
- Override: Ghi đè phương thức
