cnt = 0
for l1 in ('РУЛКА'):
    for l2 in ('РУЛЬКА'):
        for l3 in ('РУЛЬКА'):
            for l4 in ('РУЛЬКА'):
                for l5 in ('РУЛЬКА'):
                    for l6 in ('РУЛЬКА'):
                        word = l1 + l2 + l3 + l4 + l5 + l6
                        if (word.count('Р') < 2 and word.count('У') < 2 and word.count('Л') < 2 and
                            word.count('Ь') < 2 and word.count('К') < 2 and word.count('А') < 2):
                            if word[word.find('Ь')-1] != 'У' and word[word.find('Ь')-1] != 'А':
                                cnt += 1
                                print(word)
print(cnt)