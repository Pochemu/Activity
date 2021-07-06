f = open('27-12b.txt')
n = int(f.readline())
d2 = 0
d3 = 0
d6 = 0
k = 0
for _ in range(n):
    x = int(f.readline())
    if x%6 == 0:
        d6 += 1
    elif x%2 == 0:
        d2 += 1
    elif x%3 == 0:
        d3 += 1
    else:
        k += 1
ans = d2 * d3
for i in range(1, d6+1):
    ans += n - i
print(ans)