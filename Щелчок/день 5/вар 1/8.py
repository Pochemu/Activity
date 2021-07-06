flag = False
cnt = 0
for l1 in ('ЗЖДЛКЕ'):
    for l2 in ('ЗЖДЛКЕ'):
        for l3 in ('ЗЖДЛКЕ'):
            for l4 in ('ЗЖДЛКЕ'):
                for l5 in ('ЗЖДЛКЕ'):
                    for l6 in ('ЗЖДЛКЕ'):
                        word = l1 + l2 + l3 + l4 + l5 + l6
                        if word == 'ЛЗКЗКЕ':
                            flag = True
                        elif word == 'ЛЖЛЗЖЛ':
                            exit(print(cnt-1))
                        if flag:
                            cnt += 1