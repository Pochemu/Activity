f = open('27.txt')
n = int(f.readline())
k = [0] * 12
for _ in range(n):
    x = int(f.readline())
    k1 = k.copy()
    for i in range(12):
        a = (i + x) % 12
        k1[a] += k[i]
    k1[x % 12] += 1
    k = k1.copy()
f.close()
print(k[0])