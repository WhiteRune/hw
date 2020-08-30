new_file = open('avg grades.txt', 'w', encoding='utf-8')
with open('grades.txt', encoding='utf-8') as f:
    class_sum = 0
    summary = 0
    count = 0
    count_2 = 0
    line_element = 2
    for line in f:
        count_2 += 1
        for i in range(len(line.split()) - 2):
            summary += float(line.split()[line_element])
            line_element += 1
            count += 1
        average = summary / count
        if average < 5:
            print('{:<16}'.format(line.split()[1] + ' ' + list(line.split()[0])[0] + '.'), end=' ')
            print('{:<4}'.format(round(average, 2)), end='\n')
        new_file.write('{:<16}'.format(line.split()[1] + ' ' + list(line.split()[0])[0] + '.') + ' ')
        new_file.write('{:<4}'.format(round(average, 2)) + '\n')
        class_sum += average
        count = 0
        summary = 0
        line_element = 2
    class_average = class_sum / count_2
print('Средний балл по классу:', round(class_average, 2))
new_file.close()
f.close()
