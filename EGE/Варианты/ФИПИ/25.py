cnt = 0
n = 452021
while cnt != 5:
    n += 1
    cnt_del = 0
    for i in range(int(n**0.5), 1, -1):
        if n%i == 0:
            cnt_del += 2
            d1 = i
        if i**2 == n:
            cnt_del -= 1
    if cnt_del >= 2:
        m = d1 + n//d1
        if m%7 == 3:
            cnt += 1
            print(n, m)
# 452174 226089
# 452258 226131
# 452398 226201
# 452482 226243
# 452566 226285
n = 452174