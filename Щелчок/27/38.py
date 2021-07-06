cnt = 0
for i in range(8185, 6390, -1):
    if ((i % 11 == 0 or i % 17 == 0) and
            i % 2 != 0 and i % 13 != 0 and
            i % 14 != 0 and i % 34 != 0):
        cnt += 1
        min_n = i
print(cnt, min_n)