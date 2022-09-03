# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def weekdays(a):
    if a < 6:
        return 0
    else:
        return 1


day = int(input('Insert day number: '))
if day > 7:
    print(f'There is no day number {day} in week')
else:
    if weekdays(day) == 0:
        print('Not a weekend')
    else:
        print('Its weeeeeeeekend!!')
