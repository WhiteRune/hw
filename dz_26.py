s = "AABABBAABBBAB"
s = s.replace("A", "tmp")
s = s.replace("B", "A")
s = s.replace("tmp", "B")
print(s)

