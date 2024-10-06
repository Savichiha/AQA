import math

def square(side_length):
    area = int(side_length) ** 2
    return math.ceil(area)
side = input("Введите значение стороны квадрата: ")
area = square(side)

print(f"Площадь квадрата со стороной {side} равна {area}.")