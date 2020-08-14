
words = input('Enter words to count them separately:').split()

result = {}
for i in words:
    cnt = words.count(i)
    result[i] = cnt

print(result)