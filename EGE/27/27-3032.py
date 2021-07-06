f = open('27-3202b.txt')
n = int(f.readline())
s_min = 0
s_max = 0
d_ost = [10001] * 10
for _ in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a-b)
    s_min += min(a, b)
    s_max += max(a, b)
    r = d % 10
    if r != 0:
        d_ost_check = d_ost.copy()
        for i in range(1, 10):
            r1 = (r + i)%10
            d_ost_check[r1] = min(d_ost_check[r1], d + d_ost[i])
        d_ost_check[r] = min(d_ost[r], d)
        d_ost = d_ost_check.copy()
print(s_min + d_ost[s_max % 10 - s_min % 10])