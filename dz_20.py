
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


num = int(input('Enter the year:'))
print(is_year_leap(num))
