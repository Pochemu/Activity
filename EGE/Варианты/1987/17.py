cnt = 0
for i in range(1871, 9198):
    if len(str(hex(i)))-2 != len(str(i)):
        if i%9 == 2 or i%9 == 4:
            cnt += 1
print(cnt)