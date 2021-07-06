cnt = 0
for i in range(48989, 16014, -1):
    if (i % 7 == 0 or i % 11 == 0) and i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
        cnt += 1
        min_n = i
print(cnt, min_n)