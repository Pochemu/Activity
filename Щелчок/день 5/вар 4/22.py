for i in range(1, 1000):
    x = i
    L = 0
    M = 1
    while x > 0:
        L = (x%8) * M + L
        x = x//8
        M = M*10
    sum_n = 0
    for j in str(L):
        sum_n += int(j)
    if sum_n == 15:
        print(i)
        break