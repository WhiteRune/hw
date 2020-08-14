
from random import randint
lst = [randint(0, 20) for i in range(10)]
print(lst)
C = int(input('Введите число:'))
k = int(input('Введите индекс, на который хотите поставить число:'))
j = k
lst.append(C)
for _ in range(len(lst) - (k + 1)):
    lst[j-1], lst[j] = lst[j], lst[j-1]
    j -= 1

print(lst)
