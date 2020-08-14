
from random import randint
# Задаем количество рандомных чисел для первого и второго списков
num_1 = 4
num_2 = 4

lst = [randint(0, 20) for __ in range(num_1)]
lst_2 = [randint(0, 20) for _ in range(num_2)]
lst_3 = []

lst.sort()
lst_2.sort()

print(lst, '\n', lst_2)

i = 0
j = 0
count = 0

while count != num_1 + num_2:
    if i == num_1:
        if lst_2[j] >= lst_3[count - 1]:
            lst_3.append(lst_2[j])
            count += 1
            j += 1
    elif j == num_2:
        if lst[i] >= lst_3[count - 1]:
            lst_3.append(lst[i])
            count += 1
            i += 1
    else:
        if lst[i] <= lst_2[j]:
            lst_3.append(lst[i])
            i += 1
            count += 1
        else:
            lst_3.append(lst_2[j])
            j += 1
            count += 1

print(lst_3)

