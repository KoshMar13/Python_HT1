# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти(x и y).

def quatersRev(q):
    if q == 1:
        return ('x > 0 and y > 0')
    elif q == 2:
        return ('x < 0 and y > 0')
    elif q == 3:
        return ('x < 0 and y < 0')
    elif q == 4:
        return ('x > 0 and y < 0')
    # else:
    #     return ("x = 0 and y = 0")


a = int(input("Insert quater's number: "))
print(quatersRev(a))
