cnt = 0
file = open('../Варианты/1717/24-j5.txt')  # https://kpolyakov.spb.ru/cms/files/ege-sym/24-j5.txt
for s in file:
    for i in range(len(s)-2):
        if s[i:i+3] == 'KOT':
            cnt += 1
print(cnt)