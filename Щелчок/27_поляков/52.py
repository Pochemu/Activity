f = open('27-52b.txt')
n = int(f.readline())
ost0 = [0] * 4
ost1 = [0] * 4
ost2 = [0] * 4
for _ in range(n):
    x = int(f.readline())
    if x%3 == 0:
        ost0[3] = x
        ost0.sort(reverse=True)
    elif x%3 == 1:
        ost1[3] = x
        ost1.sort(reverse=True)
    else:
        ost2[3] = x
        ost2.sort(reverse=True)
print(max(ost0[0] + ost0[1] + ost0[2], ost1[0] + ost1[1] + ost1[2], ost2[0] + ost2[1] + ost2[2], ost0[0] + ost1[0] + ost2[0]))