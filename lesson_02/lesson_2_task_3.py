import math
def square(side):
    s = side ** 2
    return math.ceil(s)
side = float(input("Сторона квадрата:"))
result = square(side)
print(f"Площадь квадрата: {square(side)}")