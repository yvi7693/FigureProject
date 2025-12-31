import math
import perimeter

print("Hello, world!")


def square_area(side: int) -> int:
    result = side ** 2

    return result


def rectangle_area(height: int, width: int) -> int | float:
    result = height * width

    return result


def circle_area(radius: int) -> int:
    result = (radius ** 2) * math.pi

    return result


choice = int(input("Что будем считать?\n1 - квадрат\n2 - прямоугольник\n3 - круг\n>>"))

if choice == 1:

    side = int(input("Введите сторону квадрата >>"))

    print("Площадь: ", square_area(side))
    print("Периметр: ", perimeter.square_perimeter(side))

elif choice == 2:

    height = int(input("Введите высоту >>"))
    width = int(input("Введите ширину >>"))

    print("Площадь: ", rectangle_area(height, width))
    print("Периметр: ", perimeter.rectangle_perimeter(height, width))

elif choice == 3:

    radius = int(input("Введите радиус >>"))

    print("Площадь: ", circle_area(radius))
    print("Периметр: ", perimeter.circle_perimeter(radius))

else:
    print("Команда не корректна!!!")


