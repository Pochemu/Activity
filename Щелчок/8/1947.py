# Маша составляет 7-буквенные коды из букв А, Й, С, Б, Е, Р, Г.
# Каждую букву нужно использовать ровно 1 раз, при этом буква Й не может стоять на
# первом месте и перед гласной. Сколько различных кодов может составить Маша?
cnt = 0
for l1 in ('АСБЕРГ'):
    for l2 in ('АЙСБЕРГ'):
        for l3 in ('АЙСБЕРГ'):
            for l4 in ('АЙСБЕРГ'):
                for l5 in ('АЙСБЕРГ'):
                    for l6 in ('АЙСБЕРГ'):
                        for l7 in ('АЙСБЕРГ'):
                            word = l1 + l2 + l3 + l4 + l5 + l6 + l7
                            ok = 1
                            for i in ('АЙСБЕРГ'):
                                if word.count(i) > 1:
                                    ok = 0
                            if ok == 1:
                                if word.index('Й') != 6:
                                    if word[word.index('Й')+1] != ('А') and word[word.index('Й')+1] != ('Е'):
                                        cnt += 1
                                else:
                                    cnt += 1
print(cnt)