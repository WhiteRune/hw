
def triangle_1(height_1):
    void_space = ' '
    star = '*'
    i = 1
    space_tmp = 0
    while i != height_1:
        if i == 1:
            print(void_space * (height_1 - i) + star)
            i += 1
        else:
            print(void_space * (height_1 - i) + star + void_space * (1 + 2 * space_tmp) + star)
            space_tmp += 1
            i += 1
    print(star * (2 * height_1 - 1))


def triangle_2(height_2):
    void_space = ' '
    star = '*'
    i = 1
    space_tmp = 0
    while i != height_2:
        if i == 1:
            print(void_space * (height_2 - i) + star)
            i += 1
        else:
            print(void_space * (height_2 - i) + star + star * (1 + 2 * space_tmp) + star)
            space_tmp += 1
            i += 1
    print(star * (2 * height_2 - 1))


def square_1(height_3):
    r = height_3
    if height_3 % 2 == 0:
        height_3 //= 2
    else:
        height_3 = (height_3 + 1) // 2
    round(height_3)
    void_space = ' '
    star = '*'
    i = 1
    i2 = 1
    while i <= height_3:
        print(void_space * (height_3 - i) + star * i2)
        if i == height_3 and r % 2 == 0:
            print(void_space * (height_3 - i) + star * i2)
        i += 1
        i2 += 2
    i3 = i - 2
    i2 -= 4
    while i3 != 1:
        print(void_space * (height_3 - i3) + star + void_space * (i2 - 2) + star)
        i3 -= 1
        i2 -= 2
    print(void_space * (height_3 - i3) + star + void_space * (i2 - 2))


def square_2(height_4):
    r = height_4
    if height_4 % 2 == 0:
        height_4 //= 2
    else:
        height_4 = (height_4 + 1) // 2
    round(height_4)
    void_space = ' '
    star = '*'
    i = 1
    i2 = 1
    while i <= height_4:
        print(void_space * (height_4 - i) + star * i2)
        if i == height_4 and r % 2 == 0:
            print(void_space * (height_4 - i) + star * i2)
        i += 1
        i2 += 2
    i3 = i - 2
    i2 -= 4
    while i3 != 1:
        print(void_space * (height_4 - i3) + star + void_space * ((i2 - 2) // 2) + star + void_space * ((i2 - 2) // 2) +
              star)
        i3 -= 1
        i2 -= 2
    print(void_space * (height_4 - i3) + star + void_space * (i2 - 2))


triangle_1(int(input('Enter a height of first triangle:')))
triangle_2(int(input('Enter a height of second triangle:')))
square_1(int(input('Enter a height of first square:')))
square_2(int(input('Enter a height of second square:')))
