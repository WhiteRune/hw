
N = int(input('Введите целое число: '))
osnova_stepeni = 2
stepen = 1

while osnova_stepeni <= N:
    osnova_stepeni *= 2
    stepen += 1
print(stepen-1, osnova_stepeni // 2, '\n2 **', stepen-1, ' = ', osnova_stepeni // 2)
