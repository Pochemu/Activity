ans = 0
max_del = 0
for i in range(568_023, 569_231):
    cnt_del = 0
    for j in range(1, int(i**0.5) + 1):
        if i%j == 0:
            cnt_del += 2
        if i == j**2:
            cnt_del -= 1
    if max_del < cnt_del:
        max_del = cnt_del
        ans = i
print(max_del, ans)