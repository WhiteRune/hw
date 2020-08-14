
c = float(input('Enter a lenght of square side:'))


def square(length):
    return (4 * length,
            length ** 2,
            round(length * 2 ** (1 / 2), 2))


print(square(c))
