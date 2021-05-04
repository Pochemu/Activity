f = open('27-16b.txt')
n = int(f.readline())
d_13_d_2 = 0
d_13_n_2 = 0
n_13_d_2 = 0
n_13_n_2 = 0
ans = 0
for _ in range(n):
    x = int(f.readline())
    if x % 2 == 0:
        if x % 13 == 0:
            ans += d_13_n_2 + n_13_n_2
            d_13_d_2 += 1
        else:
            ans += d_13_n_2
            n_13_d_2 += 1
    else:
        if x % 13 == 0:
            ans += d_13_d_2 + n_13_d_2
            d_13_n_2 += 1
        else:
            ans += d_13_d_2
            n_13_n_2 += 1
print(ans)