file = open('../В процессе/24-5.txt')  # https://kpolyakov.spb.ru/cms/files/ege-sym/24-5.txt
cnt = 0
for s in file:
    for i in range (len(s)-1):
        if s[i:i+2] == '()':
            cnt += 1
        if cnt == 10000:
            print(i+1)
            break
file.close()