cnt = 0
for i in range(10837, 13921):
    if i%17 == 0 and i%7 and i%15 and i%18 and i%34:
        cnt += 1
        max_n = i
print(cnt, max_n)