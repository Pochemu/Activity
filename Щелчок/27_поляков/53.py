f = open('27-53b.txt')
n = int(f.readline())
ost0 = [10000000001] * 4
ost1 = [10000000001] * 4
ost2 = [10000000001] * 4
for _ in range(n):
    x = int(f.readline())
    if x%3 == 0:
        ost0[3] = x
        ost0.sort()
    elif x%3 == 1:
        ost1[3] = x
        ost1.sort()
    else:
        ost2[3] = x
        ost2.sort()
print(ost0)
print(ost1)
print(ost2)
print(min(ost0[0] + ost0[1] + ost0[2], ost1[0] + ost1[1] + ost1[2], ost2[0] + ost2[1] + ost2[2], ost0[0] + ost1[0] + ost2[0]))