
from random import randint
lst = [randint(0, 20) for i in range(10)]
print(lst)
k = int(input('Введите индекс элемента, который хотите удалить: '))
j = k
for _ in range(len(lst) - (k + 1)):
    lst[j+1], lst[j] = lst[j], lst[j+1]
    j += 1
lst.pop()
print(lst)
