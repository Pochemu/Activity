f = open('shkolkovo_4.txt')
cnt = 1
cnt_max = 1
ans = ''
d1 = 0
d2 = 0
max_l = 0
min_l = 100000000
ans_l = 0
for s in f:
    for i in range(2, len(s)):
        if s[i] == s[i-1] and s[i-1] != s[i-2]:
            d1 = i-1
        else:
            if s[i-1] == s[i-2]:
                d2 = i-2
            if max_l < d2 - d1 + 1:
                max_l = d2 - d1 + 1
                ans = s[i-1]
print(ans, ans_l)
