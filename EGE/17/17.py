cnt = 0
for i in range(345678, 456790):
    sum_i = 0
    for k in str(i):
        sum_i += int(k)
    if i % sum_i == 0:
        print(i)
        cnt += 1
print(cnt)