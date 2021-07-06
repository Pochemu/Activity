f = open('test.txt')
n = int(f.readline())
ost = [1000000000000000000] * 50
ind = [-1] * 50
s = 0
sum_max = 0
l_min = 0
for i in range(n):
    x = int(f.readline())
    s += x
    d = s%50
    if d == 0:
        sum_max = s
        l_min = i + 1
    else:
        if sum_max > s - ost[d]:
            sum_max = s - ost[d]
            l_min = i - ind[d]
        if sum_max == s - ost[d]:
            l_min = min(l_min, i - ind[d])
    if ost[d] > s:
        ost[d] = s
        ind[d] = i
print(sum_max, l_min)