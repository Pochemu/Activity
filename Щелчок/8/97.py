cnt = 0
flag = False
for l1 in ('ЖЗДМИЕЛП'):
    for l2 in ('ЖЗДМИЕЛП'):
        for l3 in ('ЖЗДМИЕЛП'):
            for l4 in ('ЖЗДМИЕЛП'):
                for l5 in ('ЖЗДМИЕЛП'):
                    for l6 in ('ЖЗДМИЕЛП'):
                        for l7 in ('ЖЗДМИЕЛП'):
                            for l8 in ('ЖЗДМИЕЛП'):
                                word = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                if word == 'ЕЗЗЕИДЖЗ':
                                    flag = True
                                elif word == 'ПЗИИПМЖЗ':
                                    exit(print(cnt-1))
                                if flag:
                                    cnt += 1