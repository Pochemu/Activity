cnt = 0
for i in range(14535, 32231):
    x = i
    cnt_del = set()
    d = 2
    while d ** 2 <= x:
        while x % d == 0:
            cnt_del.add(d)
            x = x//d
        d = d+1
    if x > 1:
        cnt_del.add(x)
    if len(cnt_del) == 3:
        cnt += 1
        max_n = i
print(cnt, max_n)