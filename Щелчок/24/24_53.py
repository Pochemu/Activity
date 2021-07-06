f = open('shkolkovo_3.txt')
cnt = 1
cnt_max = 1
cnt_s = 0
ans = ''
for s in f:
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if cnt_max < cnt:
                cnt_max = cnt
                ans = s[i-1]
            cnt = 1
print(ans, cnt_max)