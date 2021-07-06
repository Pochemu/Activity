cnt = 0
for i in range(9405, 7285, -1):
    if i % 13 == 0 and i % 15 == 0 and i%7 and i%17 and i%20 and i%27:
        min_n = i
        cnt += 1
print(cnt, min_n)