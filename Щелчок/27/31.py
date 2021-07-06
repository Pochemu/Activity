cnt = 0
for i in range(1721, 4323):
    if (i%3 == 0 and i%11 == 0) and i%5 and i%9 and i%13 and i%22:
        cnt += 1
        max_n = i
print(cnt, max_n)