f = open('27-37b.txt')
n = int(f.readline())
num = []
sums = set()
count_sums = [0] * 20001
cnt = 0
c = 1
for _ in range(n):
    c += 1
    print(c)
    x = int(f.readline())
    if x in sums:
        cnt += count_sums[x]
    for i in num:
        sums.add(i + x)
        count_sums[i+x] += 1
    num.append(x)
print(cnt)