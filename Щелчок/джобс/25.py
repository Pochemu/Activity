cnt = 0
for i in range(500000, 100000000000000):
    for j in range(9, i):
        if i%j == 0:
            if j%10 == 8:
                cnt += 1
                print(i, j)
                break
    if cnt == 5:
        break