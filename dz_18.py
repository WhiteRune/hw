
words = input('Enter words to count them separately:').split()

counter = {}
for i in words:
    for word in words:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
