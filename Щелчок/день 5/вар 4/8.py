cnt = 0
for l1 in ('ДЕМОН'):
    for l2 in ('ДЕМОН'):
        for l3 in ('ДЕМОН'):
            for l4 in ('ДЕМОН'):
                for l5 in ('ДЕМОН'):
                    word = l1 + l2 + l3 + l4 + l5
                    if (word.count('Д') == 1 and word.count('Е') == 1 and
                            word.count('М') == 1 and word.count('О') == 1 and word.count('Н') == 1):
                        if (word[0] == 'Е' or word[0] == 'О'):
                            if (word[-1] == 'Д' or word[-1] == 'М' or word[-1] == 'Н'):
                                cnt += 1
                        else:
                            cnt += 1
print(cnt)