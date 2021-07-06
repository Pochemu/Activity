i = 0
for l1 in ('ДЗЕЖИЛК'):
    for l2 in ('ДЗЕЖИЛК'):
        for l3 in ('ДЗЕЖИЛК'):
            for l4 in ('ДЗЕЖИЛК'):
                for l5 in ('ДЗЕЖИЛК'):
                    for l6 in ('ДЗЕЖИЛК'):
                        for l7 in ('ДЗЕЖИЛК'):
                            word = l1 + l2 + l3 + l4 + l5 + l6 + l7
                            i += 1
                            if word == 'ИДЗИИКЗ':
                                d1 = i
                            elif word == 'ЗЖЗДЛЕД':
                                d2 = i
print(d1 - d2 - 1)