cnt, cnt_max = 1, 1
char = None
f = open('../../В процессе/24data/k8-91.txt')
s = f.readline()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
        if cnt_max < cnt:
            cnt_max = cnt
            char = s[i]
    else:
        cnt = 1
print(char, cnt_max)