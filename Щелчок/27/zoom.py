f = open('test.txt')
n = int(f.readline())
ost = [1000000000001] * 73
ind = [-1] * 73
s = 0
sum_max = 0
lm = 0
for i in range(n):
    x = int(f.readline())
    s += x
    d = s % 73
    if s % 73 == 0:
        sum_max = max(sum_max, s)
    else:
        if s - ost[d] > sum_max:
            sum_max = s - ost[d]
            lm = i - ind[d]
    if ost[d] > s:
        ost[d] = s
        ind[d] = i
print(sum_max, lm)

