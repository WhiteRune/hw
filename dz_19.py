
def arithmetic(a, b, c):
    if c == '/':
        return round(a / b, 2)
    elif c == '*':
        return round(a * b, 2)
    elif c == '-':
        return a - b
    elif c == '+':
        return a + b
    else:
        return 'Unknown operation'


first = float(input('Enter first number: '))
second = float(input('Enter second number: '))
option = input('Input an option: ')
print(arithmetic(first, second, option))





