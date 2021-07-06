cnt = 0
for i in range(123456, 234568):
    sum_i = 0
    for k in str(i):
        sum_i += int(k)
    if i % sum_i == 0:
        print(i)
        cnt += 1
print(cnt)