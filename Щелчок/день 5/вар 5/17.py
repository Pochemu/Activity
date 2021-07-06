cnt = 0
for i in range(53634, 1032533):
    if i%23 == 0:
        sum_n = 0
        for j in str(i):
            sum_n += int(j)
        if i%sum_n != 0:
            print(i, sum_n)
            cnt += 1
            max_n = i
print(cnt, max_n)
