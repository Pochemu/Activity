f = open('27-12b.txt')
n = int(f.readline())
d_2 = 0
d_3 = 0
d_6 = 0
ans = 0
for i in range(n):
    x = int(f.readline())
    if x % 6 == 0:
        d_6 += 1
    if x % 2 == 0 and x % 3 != 0:
        d_2 += 1
    if x % 3 == 0 and x % 2 != 0:
        d_3 += 1
ans = d_6 * n - d_6*(d_6+1)/2 + d_2 * d_3
print(int(ans))