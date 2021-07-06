f = open('27-17b.txt')
n = int(f.readline())
buf = []
odd_13 = 0
even_13 = 0
odd = 0
even = 0
ans = 0
for _ in range(5):
    x = int(f.readline())
    buf.append(x)
for _ in range(5, n):
    x = int(f.readline())
    if buf[0] % 13 == 0:
        if buf[0] % 2 == 0:
            even_13 += 1
        else:
            odd_13 += 1
    else:
        if buf[0] % 2 == 0:
            even += 1
        else:
            odd += 1
    if x%13 == 0:
        if x % 2 == 0:
            ans += odd_13 + odd
        else:
            ans += even_13 + even
    else:
        if x%2 == 0:
            ans += odd_13
        else:
            ans += even_13
    buf.append(x)
    del buf[0]
print(ans)