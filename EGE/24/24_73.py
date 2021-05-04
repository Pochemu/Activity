f = open('../../../В процессе/24data/k8-4.txt')
s = f.readline()
cnt_max, cnt = 1, 1
chars = []
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        cnt += 1
        if cnt_max < cnt:
            cnt_max = cnt
            chars = [s[i]]
        elif cnt_max == cnt:
            chars.append(s[i])
    else:
        cnt = 1
for i in chars:
    print(i, cnt_max)