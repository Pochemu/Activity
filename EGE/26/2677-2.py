f = open('27-17b.txt')
n = int(f.readline())
d_13_d_2 = 0
d_13_n_2 = 0
n_13_d_2 = 0
n_13_n_2 = 0
ans = 0
buf = []
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(5, n):
    x = int(f.readline())
    if buf[0] % 2 == 0:
        if buf[0] % 13 == 0:
            d_13_d_2 += 1
        else:
            n_13_d_2 += 1
    else:
        if buf[0] % 13 == 0:
            d_13_n_2 += 1
        else:
            n_13_n_2 += 1
    if x % 2 == 0:
        if x % 13 == 0:
            ans += d_13_n_2 + n_13_n_2
        else:
            ans += d_13_n_2
    else:
        if x % 13 == 0:
            ans += d_13_d_2 + n_13_d_2
        else:
            ans += d_13_d_2
    del buf[0]
    buf.append(x)
print(ans)