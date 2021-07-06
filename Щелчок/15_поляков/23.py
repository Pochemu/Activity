r = [0] * 41
r[2] = 1
for i in range(3, 41):
    r[i] = r[i-2] + r[i//2] * (i%2 == 0)
print(r)