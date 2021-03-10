cnt = 0
for i in range(1221, 9764):
    if not i%7 and i%2 and i%5 and i%11 and i%49:
        cnt += 1
        maximum = i
print(cnt, maximum)