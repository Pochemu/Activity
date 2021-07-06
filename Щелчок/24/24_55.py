f = open('shkolkovo_5.txt')
m = []
for s in f:
    for i in range(1, len(s)-1):
        if ord(s[i]) < ord(s[i-1]) and ord(s[i]) < ord(s[i+1]):
            m.append(i)
m.sort()
print(m[-1] - m[0])