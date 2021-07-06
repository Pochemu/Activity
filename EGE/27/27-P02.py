f = open('../../../../В процессе/test.txt')
n = int(f.readline())
k = [0]*12
for _ in range(n):
    x = int(f.readline())
    k1 = k.copy()
    for i in range(12):
        k1[(i+x) % 12] += k[i]
    k1[x%12] += 1
    k = k1.copy()
print(k)