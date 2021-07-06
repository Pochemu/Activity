r = [0] * 10
r[2] = 1
print(r)
for i in range(3, 10):
    a = r[i-1]
    b = r[i-2]
    c = r[i//3] * (i%3 == 0)
    r[i] = a + b + c
for i in range(10):
    print(i, r[i])
k = [0] * 20
k[9] = r[9]
for i in range(10, 20):
    if i != 12:
        a = k[i - 1]
        b = k[i - 2]
        c = k[i // 3] * (i % 3 == 0)
        k[i] = a + b + c
print(k[19])