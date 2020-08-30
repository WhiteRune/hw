class Counter:
    current = 0

    def __init__(self, min_value=None, max_value=None):
        self.start = min_value
        self.end = max_value

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            return 'Out of range'

    def reset(self):
        self.current = 0
        return 'Succesfully reset!'


my_count = Counter(min_value=0, max_value=21)
inc = 0
while inc != 'Out of range':
    inc = my_count.increase()
    print(inc)
# Убеждаемся, что счетчик уперся в потолок и ресетим, затем проверяем
print(my_count.increase())
print(my_count.reset())
print(my_count.increase())


