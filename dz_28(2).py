f = open('input_data.txt', 'w', encoding='utf-8')
data = ' '
while data != '':
    data = input()
    f.write(data + '\n')

f.close()
