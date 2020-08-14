
date = int(input('Введите год:'))

if date <= 0:
    print('Вернитесь и введите положительное значение')
elif date % 400 == 0:
    print('Год високосный')
elif date % 100 == 0:
    print('Год невисокосный')
elif date % 4 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')