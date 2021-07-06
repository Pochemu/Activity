cnt = 0
for i in range(8367, 1169, -1):
    if (i%3 == 0 or i % 7 == 0) and i%11 and i%13 and i%17 and i%19:
        cnt += 1
        min_n = i
print(cnt, min_n)