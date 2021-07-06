f = open('27-19b.txt')
n = int(f.readline())
max_m = 0
p = []
max_p = []
for i in range(n):
    x = int(f.readline())
    if x != 0:
        p.append(x)
    else:
        m = 1
        for i in (p):
            m = m * i
        if m > max_m:
            max_p = p
            max_m = m
        p = []
else:
    m = 1
    for i in (p):
        m = m * i
    if m > max_m:
        max_p = p
        max_m = m
print(max_m)
print(max_p)