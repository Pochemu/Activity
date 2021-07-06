cnt = 0
for l1 in 'МАШИН':
    for l2 in 'МАШИН':
        for l3 in 'МАШИН':
            for l4 in 'МАШИН':
                for l5 in 'МАШИН':
                    for l6 in 'МАШИН':
                        word = l1 + l2 + l3 + l4 + l5 + l6
                        if ('М' in word) or ('Ш' in word) or ('Н' in word):
                            if ((word.count('А') == 1 and word.count('И') == 0) or
                                    (word.count('И') == 1 and word.count('А') == 0)):
                                cnt += 1
print(cnt)
