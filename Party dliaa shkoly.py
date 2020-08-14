k1 = input('Введите количество учеников в 1м классе:')
k2 = input('Введите количество учеников в 2м классе:')
k3 = input('Введите количество учеников в 3м классе:')

k_1 = int(k1)
k_2 = int(k2)
k_3 = int(k3)

ostatok_1 = k_1 % 2
ostatok_2 = k_2 % 2
ostatok_3 = k_3 % 2

desks_1 = k_1 // 2 + ostatok_1
desks_2 = k_2 // 2 + ostatok_2
desks_3 = k_3 // 2 + ostatok_3

desks_sum = desks_1 + desks_2 + desks_3

print('Кол-во парт для 1-го класса:\n', desks_1,
      '\nКол-во парт для 2-го класса:\n', desks_2,
      '\nКол-во парт для 3-го класса:\n', desks_3,
      '\nНеобходимое количество парт для всех учеников:\n',
      desks_sum)


