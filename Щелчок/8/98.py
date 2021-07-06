cnt = 0
flag = False
for l1 in ('ДКЕЖНМ'):
    for l2 in ('ДКЕЖНМ'):
        for l3 in ('ДКЕЖНМ'):
            for l4 in ('ДКЕЖНМ'):
                for l5 in ('ДКЕЖНМ'):
                    for l6 in ('ДКЕЖНМ'):
                        word = l1 + l2 + l3 + l4 + l5 + l6
                        if word == 'ЖЕДЕЕК':
                            flag = True
                        elif word == 'МЕДЕНН':
                            exit(print(cnt-1))
                        if flag:
                            cnt += 1