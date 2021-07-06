f = open('24.txt')
l = 0
max_l = 0
for s in f:
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
            l += 1
            max_l = max(l, max_l)
        else:
            l = 0
    else:
        max_l = max(l, max_l)
print(max_l)