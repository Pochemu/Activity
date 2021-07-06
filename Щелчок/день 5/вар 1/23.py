r = [0]*26
r[2] = 1
for i in range(3, 26):
    if i != 19:
        r[i] += r[i-1] + r[i//2] * (i%2 == 0) + r[i//3] * (i%3 == 0)
print(r)