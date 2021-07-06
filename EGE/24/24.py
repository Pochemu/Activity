max_length = []
f = open('24.txt')
for s in (f):
    if (s.count('A')) >= 25:
        max_l = [1]
        for i in range(len(s)//2):
            for j in range(len(s)-1, len(s)//2-1, -1):
                if s[i] == s[j]:
                    max_l.append(j-i)
        max_length.append(max(max_l))
print(max(max_length))
f.close()