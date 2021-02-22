f = open('../../../В процессе/24data/k7c-3.txt')
cnt = 0
s = f.readline()
for i in range(len(s)-2):
    if (s[i+1] in 'BDE'and s[i+2] in 'ACD' and
            s[i] == s[i+2] and s[i+2] != s[i+1]):
        cnt += 1
print(cnt)