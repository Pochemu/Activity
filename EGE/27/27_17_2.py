f = open('27-17a.txt')
n = int(f.readline())
buf = []
m = 1001
answer = 1000001
cnt = 0
for _ in range(5):
    buf.append(int(f.readline()))
for _ in range(5, n):
    x = int(f.readline())
f.close()