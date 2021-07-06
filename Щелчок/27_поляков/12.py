f = open('27-12b.txt')
n = int(f.readline())
k6 = 0
k3 = 0
k2 = 0
k = 0
ans = 0
for _ in range(n):
    x = int(f.readline())
    if x%6 == 0:
        ans += k + k2 + k3 + k6
        k6 += 1
    elif x%3 == 0:
        ans += k2 + k6
        k3 += 1
    elif x%2 == 0:
        ans += k3 + k6
        k2 += 1
    else:
        ans += k6
        k += 1
print(ans)