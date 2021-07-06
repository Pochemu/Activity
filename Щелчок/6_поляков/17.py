cnt = 0
for i in range(1512, 13203):
    if i % 7 == 0 and i % 11 and i % 13 and i % 17 and i % 23:
        max_n = i
        cnt += 1
print(cnt, max_n)