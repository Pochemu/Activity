cnt = 0
for i in range(500_000, 5_000_001):
    n_8 = str(oct(i))
    if '1' in n_8:
        nod = 1
        cnt += 1
    else:
        nod = 7
        ok = 0
        while ok != 1:
            for j in range(2, len(n_8)):
                x = int(n_8[j])
                if x != 0:
                    if x%nod != 0:
                        nod -= 1
                        ok = 0
                        break
                    ok = 1
        if i % nod == 0:
            cnt += 1
    print(i)
print(cnt)