file = open('../В процессе/24-s1.txt')  # https://kpolyakov.spb.ru/cms/files/ege-sym/24-s1.txt
cnt = 0
for s in file:
    for i in range(len(s) - 2):
        if s[i:i + 3:2] == 'FO':
            cnt += 1
            break
print(cnt)
