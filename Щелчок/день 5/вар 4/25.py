cnt = 0
for i in range(109_258, 815_093):
    if (i%7==0) != (i%15==0):
        cnt += 1
print(cnt)