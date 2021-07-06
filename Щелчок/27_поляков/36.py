f = open('27-36a.txt')
n = int(f.readline())
nod = 0
ost = [10001] * 10
z = [0] * 3
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    n = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            n1 = max(n, i)
    for i in range(1, min(c, b)+1):
        if c % i == 0 and b % i == 0:
            n2 = max(n, i)
    for i in range(1, min(a, c)+1):
        if a % i == 0 and c % i == 0:
            n3 = max(n, i)
    z[0] = n1
    z[1] = n2
    z[2] = n3
    z.sort()
    nod += z[2]
    ost1 = ost.copy()
    for j in range(2):
        d = z[2] - z[j]
        r = d%10
        if r != 0:
            for i in range(1, 10):
                r1 = (r + i)%10
                ost1[r1] = min(ost1[r1], d + ost[i])
            ost[r] = min(ost[r], d)
    ost = ost1.copy()
if nod % 10 == 0:
    print(nod)
else:
    print(nod - ost[nod%10])