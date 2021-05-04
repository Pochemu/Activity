f = open('24.txt')
cnt = 0
symb = 1
for s in f:
    for i in range(len(s)):
        if s[i:i+2] == '()':
            cnt += 1
            if cnt == 10000:
                print(symb)
        symb += 1
f.close()