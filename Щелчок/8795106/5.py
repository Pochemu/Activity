n = set()
for i in range(100, 3001):
    x = bin(i)
    d1 = i
    x = str(x)[2:].replace('1', '0', 1)
    d2 = int(x, 2)
    n.add(d1-d2)
print(len(n))
