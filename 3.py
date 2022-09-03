# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quaters(a, b):
    if a > 0 and b > 0:
        return 1
    elif a < 0 and b > 0:
        return 2
    elif a < 0 and b < 0:
        return 3
    elif a > 0 and b < 0:
        return 4
    # else:
    #     print("I've sad x ≠ 0 and y ≠ 0!")


x = int(input('Insert x ≠ 0: '))
y = int(input('Insert y ≠ 0: '))
print(quaters(x, y))
