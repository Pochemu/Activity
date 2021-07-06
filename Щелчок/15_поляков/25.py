for i in range(809, 1321):
    n = i**2
    cnt_del = 0
    for j in range(1, i + 1):
        if n % j == 0:
            cnt_del += 2
        if n == j**2:
            cnt_del -= 1
    if cnt_del == 5:
        print(i**2)
for k in range(1, 923522):
    if 923521 % k == 0:
        print(k)
