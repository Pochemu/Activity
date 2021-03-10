n = int(input())
table = [[] for _ in range(n)]
for i in range(n):
    table[i] = list(map(int, input().split()))
first, last = map(int, input().split())
first -= 1
last -= 1
p = [-1] * n
used = [0] * n
q = []
used[first] = 1
q.extend([first])
while len(q) != 0:
    v = q[0]
    del q[0]
    for i in range(n):
        if table[v][i] == 1 and used[i] == 0:
            p[i] = v
            used[i] = 1
            q.extend([i])
if first == last:
    print(0)
elif p[last] == -1:
    print(-1)
else:
    steps = []
    now=last
    steps.extend([now])
    while p[now] != -1:
        steps.extend([p[now]])
        now = p[now]
    print(len(steps)-1)
    for i in range(len(steps)-1, -1, -1):
        print(steps[i]+1, end=' ')
