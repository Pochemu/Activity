cnt = 0
max_answer = 0
for i in range(1512, 13203):
    if i % 7 == 0 and i % 13 != 0 and i % 11 != 0 and i % 17 != 0 and i % 23 != 0:
        cnt += 1
        max_answer = i
print(cnt, max_answer)
