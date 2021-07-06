cnt = 0
for i in range(6278658, 18455, -1):
    if i % 12 == 0 and i%11 and i%13 and i%31 and i%48 and i%158 and i%191:
        cnt += 1
        min_n = i
print(cnt, min_n)