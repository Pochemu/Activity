n = int(input())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
first, last = map(int, input().split())
if first == last:
    exit(print(0))
first -= 1
last -= 1
p = [-1] * n
used = [0] * n
used[first] = 1
q = [first]
while len(q) != 0:
    v = q[0]
    del q[0]
    for i in range(n):
        if matrix[v][i] == 1 and used[i] == 0:
            p[i] = v
            used[i] = 1
            q.append(i)
if p[last] == -1:
    print(-1)
else:
    steps = []
    now = last
    steps.append(now)
    while p[now] != -1:
        now = p[now]
        steps.append(now)
    print(len(steps)-1)
    for i in range(len(steps)-1, -1, -1):
        print(steps[i]+1, end=' ')