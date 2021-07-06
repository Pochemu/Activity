def find(n):
    min_num = 10
    max_num = 0
    for i in str(n):
        min_num = min(min_num, int(i))
        max_num = max(max_num, int(i))
    return max_num - min_num


cnt = 0
for i in range(147870, 1004, -1):
    if not('1' in str(i)):
        if find(i) < 4:
            cnt += 1
            if cnt == 25:
                print(i)
print(cnt)