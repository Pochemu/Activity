cnt = 0
for i in range(9913, 13895):
    if (i%3 == 0) and (i%7 == 0) and (i%4 != 0) and (i%17 != 0) and (i%23 != 0) and (i%42 != 0):
        cnt += 1
        max_n = i
print(cnt, max_n)