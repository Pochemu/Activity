f = open('27-54b.txt')
n = int(f.readline())
ost0 = [-10000] * 5
ost1 = [-10000] * 5
ost2 = [-10000] * 5
ost3 = [-10000] * 5

for _ in range(n):
    x = int(f.readline())
    if x % 4 == 0:
        ost0[4] = x
        ost0.sort(reverse=True)
    if x % 4 == 1:
        ost1[4] = x
        ost1.sort(reverse=True)
    if x % 4 == 2:
        ost2[4] = x
        ost2.sort(reverse=True)
    if x % 4 == 3:
        ost3[4] = x
        ost3.sort(reverse=True)
ans = 0
ost = ost0 + ost1 + ost2 + ost3
for k1 in range(len(ost)-3):
    for k2 in range(k1+1, len(ost)-2):
        for k3 in range(k2+1, len(ost)-1):
            for k4 in range(k3+1, len(ost)):
                if (ost[k1] + ost[k2] + ost[k3] + ost[k4])%4 == 0:
                    n = ost[k1] + ost[k2] + ost[k3] + ost[k4]
                    ans = max(ans, n)
print(ans)