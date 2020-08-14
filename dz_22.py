
def season(month):
    if month <= 0:
        return 'ne nado, takogo mesyatsa net'
    if 0 < month < 3 or month == 12:
        return "Winter"
    if 3 <= month < 6:
        return "Spring"
    if 6 <= month < 9:
        return "Summer"
    if 9 <= month < 12:
        return "Autumn"


num = int(input('Enter the number of month:'))
print(season(num))
