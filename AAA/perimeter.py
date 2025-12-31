import math


def square_perimeter(side: int) -> int:
    result = side * 4

    return result


def rectangle_perimeter(height: int, width: int) -> int:
    result = (2 * height) + (2 * width)

    return result


def circle_perimeter(radius: int) -> int | float:
    result = 2 * math.pi * radius

    return result
