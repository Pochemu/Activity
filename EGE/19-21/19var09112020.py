for x in range(1, 100):
    answer = x
    L = 0
    M = 1
    while x > 0:
        L = x % 10 * M + L
        x = x//10
        M = M * 10
    L = str(L)
    sum_l = 0
    for i in L:
        sum_l += int(i)
    if sum_l == 15:
        print(answer)
