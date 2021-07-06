file = open('../Варианты/1717/24-j5.txt', 'r')  # https://kpolyakov.spb.ru/cms/files/ege-sym/24-j5.txt
cnt = 0
for s in file:
    for i in range(len(s)-4):
        if s[i:i+5] == 'SOCKS':
            cnt += 1
print(cnt)
file.close()