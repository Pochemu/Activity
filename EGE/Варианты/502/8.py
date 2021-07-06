l = ['Р', 'У', 'С', 'Л', 'А', 'Н']
cnt = 0
for i1 in range(6):
    for i2 in range(6):
        for i3 in range(6):
            for i4 in range(6):
                for i5 in range(6):
                    word = l[i1] + l[i2] + l[i3] + l[i4] + l[i5]
                    if word.count('У') <= 1 and word.count('А') <= 1:
                        cnt += 1
print(cnt)