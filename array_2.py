from random import randint
M = int(input('Enter a width and also height of the array: '))
lst = []
array = [[randint(1, 50) for _ in range(M)] for tmp in range(M)]

for i in range(M):
    lst.append(0)
    for j in range(M):
        lst[i] += array[j][i]

print("Before sorting:")
for i in range(M):
    for j in range(M):
        print('{:>4}'.format(array[i][j]), end=' ')
    print('\n')
for i in range(M):
    print('{:>4}'.format(lst[i]), end=' ')
print('\n\n\n')

for i in range(M-1):
    for j in range(M-i-1):
        if lst[j] >= lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            for _ in range(M):
                array[_][j], array[_][j+1] = array[_][j+1], array[_][j]

for i in range(M):
    if i % 2 == 0:
        for j in range(M-1):
            for _ in range(M-j-1):
                    if array[_][i] <= array[_+1][i]:
                        array[_][i], array[_+1][i] = array[_+1][i], array[_][i]
    else:
        for j in range(M-1):
            for _ in range(M-j-1):
                    if array[_][i] >= array[_+1][i]:
                        array[_][i], array[_+1][i] = array[_+1][i], array[_][i]

print('After sorting:')
for i in range(M):
    for j in range(M):
        print('{:>4}'.format(array[i][j]), end=' ')
    print('\n')
for i in range(M):
    print('{:>4}'.format(lst[i]), end=' ')




