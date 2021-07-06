r = [0] * 100
r[5] = 1
for i in range(7, 100):
    r[i] = r[i-2] + r[i-5]
    if r[i] == 34:
        print(i)
print(r)