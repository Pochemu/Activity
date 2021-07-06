answer =[0, 0]
count_del = 0
for i in range(394441, 394506):
    for j in range(1, int(i**0.5)):
        if i%j == 0:
            count_del += 2
    if i%(i**0.5)==0:
        count_del += 1
    if count_del > answer[0]:
        answer[0] = count_del
        answer[1] = i
        print(*answer)
print(*answer)