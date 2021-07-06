cnt = 0
for l1 in ('ШАНЕЛ'):
    for l2 in ('ШАНЕЛЬ'):
        for l3 in ('ШАНЕЛЬ'):
            for l4 in ('ШАНЕЛЬ'):
                for l5 in ('ШАНЕЛЬ'):
                    for l6 in ('ШАНЕЛЬ'):
                        word = l1+l2+l3+l4+l5+l6
                        if (word.count('Ш') == 1 and word.count('А') == 1 and
                            word.count('Н') == 1 and word.count('Е') == 1 and
                            word.count('Л') == 1 and word.count('Ь') == 1):
                            if not('ЕАЬ' in word):
                                cnt += 1
print(cnt)