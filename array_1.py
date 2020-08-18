from random import randint
M = int(input('Enter a width of array: '))
N = int(input('Enter a height of array: '))
summary = 0
lst = []
array = [[randint(10, 50) for _ in range(M)] for l in range(N)]

for i in range(N):
    for j in range(M):
        summary += array[i][j]
    array[i].append(summary)
    summary = 0

for j2 in range(M):
    for i2 in range(N):
        summary += array[i2][j2]
    lst.append(summary)
    summary = 0

for m1 in range(N):
    for n2 in range(M + 1):
        print('{:>4}'.format(array[m1][n2]), end=' ')
    print('\n')

for r in range(M):
    print('{:>4}'.format(lst[r]), end=' ')
