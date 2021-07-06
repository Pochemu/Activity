f = open('test.txt')
n = int(f.readline())
sum_max = 0
s = 0
ost = [10000000000000001] * 50
ind = [-1] * 50
lm = 0
for i in range(n):
    x = int(f.readline())
    s = s+x
    d = s%50
    if d == 0:
        sum_max = s
        lm = i + 1
    else:
        if sum_max < s:
            sum_max = s - ost[d]
            lm = i - ind[d]
        if sum_max == s - ost[d]:
            lm = min(lm, i - ind[d])
    if ost[d] > s:
        ost[d] = s
        ind[d] = i
print(sum_max)