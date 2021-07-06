cnt = 0
for i in range(10414, 4667, -1):
    if (i%3 == 0 or i%11 == 0) and i%2 and i%13 and i%22 and i%33:
        cnt += 1
        min_n = i
print(cnt, min_n)