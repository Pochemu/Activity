cnt = 0
for i in range(9405, 7285, -1):
    if i % 15 == 0 and i % 13 == 0 and i % 7 != 0 and i % 17 != 0 and i % 20 != 0 and i % 27 != 0:
        cnt += 1
        answer = i
print(cnt, answer)