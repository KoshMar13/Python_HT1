# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def TrueCheck(a, b, c):
    left = (not (a or b or c))
    right = ((not a) and (not b) and (not c))
    return left == right

# ручной режим
# x = (input('Insert first predicate (0 or 1): '))
# y = (input('Insert second predicate (0 or 1): '))
# z = (input('Insert third predicate (0 or 1): '))
# print(TrueCheck(x, y, z))


# автоматический режим
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            x = bool(x)
            y = bool(y)
            z = bool(z)
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - {TrueCheck(x, y, z)}')
