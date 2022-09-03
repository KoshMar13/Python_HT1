# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def LineLength(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    line = round((x**2 + y**2)**0.5, 2)
    return line


point1 = list(map(float, input("Insert first point's coordinates: ").split()))
point2 = list(map(float, input("Insert second point's coordinates: ").split()))

print(LineLength(point1, point2))
