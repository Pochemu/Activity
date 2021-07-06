f = open('test.txt')
cnt = 0
ans = 0
for s in f:
    for i in range(1, len(s)):
        cnt += 1
        if s[i] == 'D' and s[i-1] == 'A' or s[i] == 'A' and s[i-1] == 'D':
            ans = max(ans, cnt-2)
            cnt = 0
print(ans)