cnt = 0
for l1 in 'ОДЕВФЦРЧГ':
    for l2 in 'ОДЕВФЦРЧГ':
        for l3 in 'ОДЕВФЦРЧГ':
            for l4 in 'ОДЕВФЦРЧГ':
                for l5 in 'ОДЕВФЦРЧГ':
                    for l6 in 'ОДЕВФЦРЧГ':
                        word = l1 + l2 + l3 + l4 + l5 + l6
                        flag = True
                        for i in 'ОДЕВФЦРЧГ':
                            if word.count(i) > 1:
                                flag = False
                        if flag:
                            cnt += 1
print(cnt)
