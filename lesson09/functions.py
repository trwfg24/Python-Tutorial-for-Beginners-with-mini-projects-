def hello_world():
    print("Hello world!")


hello_world()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


total = sum()
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mul_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mul_named_items(first="Dave", last="John")
