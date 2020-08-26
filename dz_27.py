c = 0
s = '2787'
k = list(s)
for i in enumerate(k):
    c += int(k[i][1])*(i+1)
    print(i)