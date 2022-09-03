# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def TrueCheck(a, b, c):
    left = bool(not (a+b+c))
    right = bool(not a*(not b)*(not c))
    return left == right

# ручной режим
# x = bool(int(input('Insert first predicate (0 or 1): ')))
# y = bool(int(input('Insert second predicate (0 or 1): ')))
# z = bool(int(input('Insert third predicate (0 or 1): ')))
# print(TrueCheck(x, y, z))


# автоматический режим
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            x = bool(x)
            y = bool(y)
            z = bool(z)
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - {TrueCheck(x, y, z)}')
