cnt = 0
for i in range(8812, 12286):
    if ((i % 8 == 0 or i % 19 == 0) and
            i % 4 != 0 and i % 9 != 0 and
            i % 14 != 0 and i % 16 != 0):
        max_n = i
        cnt += 1
print(cnt, max_n)
