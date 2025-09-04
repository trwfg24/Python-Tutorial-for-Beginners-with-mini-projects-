# Định nghĩa class Vehicle (Phương tiện giao thông) - đây là class cha (parent class)
class Vehicle:
    # Phương thức __init__ được gọi khi tạo một object mới (constructor)
    def __init__(self, make, model):
        self.make = make  # Thuộc tính hãng sản xuất
        self.model = model  # Thuộc tính mẫu xe

    # Phương thức để mô tả cách di chuyển của phương tiện
    def moves(self):
        print("Moves along..")

    # Phương thức để hiển thị thông tin hãng và mẫu xe
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


# Tạo object (instance) từ class Vehicle
my_car = Vehicle("Tesla", "Model 2")
# print(my_car.make)     # Có thể truy cập thuộc tính trực tiếp
# print(my_car.model)    # Nhưng thường dùng phương thức để truy cập
my_car.get_make_model()  # Gọi phương thức để hiển thị thông tin
my_car.moves()  # Gọi phương thức di chuyển

# Tạo object thứ hai từ cùng class
your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


# INHERITANCE (Kế thừa) - Tạo class con kế thừa từ class cha


# Class Airplane kế thừa từ Vehicle
class Airplane(Vehicle):
    # Override constructor để thêm thuộc tính riêng
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # Gọi constructor của class cha
        self.faa_id = faa_id  # Thuộc tính riêng của máy bay

    # Override phương thức moves() để có hành vi riêng
    def moves(self):
        print("Flies along..")


# Class Truck kế thừa từ Vehicle
class Truck(Vehicle):
    # Chỉ override phương thức moves(), giữ nguyên constructor
    def moves(self):
        print("Rumbles along..")


# Class GolfCart kế thừa từ Vehicle nhưng không thay đổi gì
class GolfCart(Vehicle):
    pass  # Từ khóa pass có nghĩa là không làm gì thêm


# Tạo các object từ các class con
cessna = Airplane("Cessna", "Syhawk", "V-12345")  # Có thêm tham số faa_id
mack = Truck("Mack", "Pinnacle")  # Chỉ cần make và model
golfwagon = GolfCart("Ymaha", "GC100")  # Giống như Vehicle

# Test các object
cessna.get_make_model()  # Kế thừa từ Vehicle
cessna.moves()  # LỖI: Quên gọi () - nên là cessna.moves()

mack.get_make_model()  # Kế thừa từ Vehicle
mack.moves()  # Override - in "Rumbles along.."

golfwagon.get_make_model()  # Kế thừa từ Vehicle
golfwagon.moves()  # Kế thừa - in "Moves along.."

print("\n\n")

# POLYMORPHISM (Đa hình) - Cùng một phương thức nhưng hành vi khác nhau
# Duyệt qua tất cả các object và gọi cùng các phương thức
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()  # Tất cả đều có phương thức này (từ Vehicle)
    v.moves()  # Mỗi class có cách thực hiện khác nhau
