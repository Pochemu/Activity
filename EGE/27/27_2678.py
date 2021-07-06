f = open('27-2678b.txt')
n = int(f.readline())
buf = []
even = 0
odd = 0
even_13 = 0
odd_13 = 0
ans = 0
for _ in range(4):
    x = int(f.readline())
    buf.append(x)
    if x % 13 == 0:
        if x % 2 == 0:
            ans += odd
            even_13 += 1
            even += 1
        else:
            ans += even
            odd_13 += 1
            odd += 1
    else:
        if x % 2 == 0:
            ans += odd_13
            even += 1
        else:
            ans += even_13
            odd += 1
for _ in range(4, n):
    x = int(f.readline())
    if x % 13 == 0:
        if x % 2 == 0:
            ans += odd
            even_13 += 1
            even += 1
        else:
            ans += even
            odd_13 += 1
            odd += 1
    else:
        if x % 2 == 0:
            ans += odd_13
            even += 1
        else:
            ans += even_13
            odd += 1
    if buf[0] % 13 == 0:
        if buf[0] % 2 == 0:
            even_13 -= 1
            even -= 1
        else:
            odd_13 -= 1
            odd -= 1
    else:
        if buf[0] % 2 == 0:
            even -= 1
        else:
            odd -= 1
    del buf[0]
    buf.append(x)
print(ans)