

# Pythagorean table
for val1 in range(1, 10):
    for val2 in range(1, 10):
        if val1 == 1 and val2 == 1:
            print('', end='    ')
            continue
        if val1 == 1:
            print(val2, end='   ')
            continue

        print('{:<4}'.format(val1*val2), end='')