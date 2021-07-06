f = open('test.txt')
n = int(f.readline())
ost = [1000000000000001] * 71
ind = [-1] * 71
lm = 0
sum_max = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    d = s%71
    if d == 0:
        sum_max = max(sum_max, s)
    elif s - ost[d] > sum_max:
        sum_max = s - ost[d]
        lm = i - ind[d]
    if ost[d] > s:
        ost[d] = s
        ind[d] = i
print(sum_max, lm)
