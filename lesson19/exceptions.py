# Bài 19: Xử Lý Ngoại Lệ trong Python


# Tạo một lớp ngoại lệ tùy chỉnh
# Các ngoại lệ tùy chỉnh nên kế thừa từ lớp Exception
class JustNotCoolError(Exception):
    """
    Một lớp ngoại lệ tùy chỉnh để minh họa.
    Điều này cho thấy cách tạo các loại ngoại lệ của riêng bạn.
    """

    pass


# Khởi tạo một biến để kiểm tra
x = 2

# Minh họa khối try-except-else-finally
try:
    # Raise một ngoại lệ tùy chỉnh
    raise JustNotCoolError("This just isn't cool, man.")

    # Các ví dụ khác về ngoại lệ phổ biến (được comment):
    # print(x / 1)  # Điều này sẽ gây ra ZeroDivisionError nếu x/0
    # if not type(x) is str:
    #     raise TypeError("Chỉ cho phép kiểu chuỗi.")
    # raise Exception("Tôi là một ngoại lệ tùy chỉnh!")

# Xử lý các loại ngoại lệ cụ thể
except NameError:
    # NameError xảy ra khi một biến không được định nghĩa
    print("NameError có nghĩa là có gì đó có thể chưa được định nghĩa.")

except ZeroDivisionError:
    # ZeroDivisionError xảy ra khi chia cho zero
    print("Vui lòng không chia cho zero.")

except Exception as error:
    # Điều này bắt tất cả các ngoại lệ khác
    # Mệnh đề 'as error' bắt đối tượng ngoại lệ
    print(f"Đã xảy ra ngoại lệ: {error}")

else:
    # Khối else chỉ chạy khi không có ngoại lệ nào được raise
    print("Không có lỗi!")

finally:
    # Khối finally luôn chạy, bất kể có ngoại lệ hay không
    print("Tôi sẽ in ra với hoặc không có lỗi.")
