
lst = [[34587, 'Learning Python, Mark Lutz', 4, 40.95], [98762, 'Programming Python, Mark Lutz', 5, 56.80],
       [77226, 'Head First Python, Paul Barry', 3, 32.95], [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

order_num = []
qtt = []
price = []
for i in range(4):
    order_num.append(lst[i][0])
    qtt.append(lst[i][2])
    price.append(lst[i][3])


print(
    list(
        map(
            lambda a, c, d: (a, round(c * d, 2) + 10 if c * d < 100 else round(c * d, 2)), order_num, qtt, price
        )
    )
)

