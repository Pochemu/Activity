cnt = 0
for i in range(14454, 1739, -1):
    if i % 4 == 0 and i%5 == 0 and i%8 and i%12 and i%16 and i%30:
        cnt += 1
        min_n = i
print(cnt, min_n)