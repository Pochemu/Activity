def do_and_check_steps():
    global v, used, p, q
    if v[0] >= 2 and v[1] >= 1 and used[v[0]-2][v[1]-1] == 0:
        p[v[0]-2][v[1]-1] = v
        used[v[0]-2][v[1]-1] = 1
        q.append([v[0]-2, v[1]-1])
    if v[0] >= 2 and v[1] <= n-2 and used[v[0]-2][v[1]+1] == 0:
        p[v[0]-2][v[1]+1] = v
        used[v[0]-2][v[1]+1] = 1
        q.append([v[0]-2, v[1]+1])
    if v[0] >= 1 and v[1] <= n-3 and used[v[0]-1][v[1]+2] == 0:
        p[v[0]-1][v[1]+2] = v
        used[v[0]-1][v[1]+2] = 1
        q.append([v[0]-1, v[1]+2])
    if v[0] >= 1 and v[1] >= 2 and used[v[0]-1][v[1]-1] == 0:
        p[v[0]-1][v[1]-2] = v
        used[v[0]-1][v[1]-1] = 1
        q.append([v[0]-1, v[1]-2])
    if v[0] <= n-3 and v[1] <= n-2 and used[v[0]+2][v[1]+1] == 0:
        p[v[0]+2][v[1]+1] = v
        used[v[0]+2][v[1]+1] = 1
        q.append([v[0]+2, v[1]+1])
    if v[0] <= n-3 and v[1] >= 1 and used[v[0]+2][v[1]-1] == 0:
        p[v[0]+2][v[1]-1] = v
        used[v[0]+2][v[1]-1] = 1
        q.append([v[0]+2, v[1]-1])
    if v[0] <= n-2 and v[1] >= 2 and used[v[0]+1][v[1]-2] == 0:
        p[v[0]+1][v[1]-2] = v
        used[v[0]+1][v[1]-2] = 1
        q.append([v[0]+1, v[1]-2])
    if v[0] <= n-2 and v[1] <= n-3 and used[v[0]+1][v[1]+2] == 0:
        p[v[0]+1][v[1]+2] = v
        used[v[0]+1][v[1]+2] = 1
        q.append([v[0]+1, v[1]+2])
n = int(input())
first = list(map(int, input().split()))
first[0] -= 1
first[1] -= 1
last = list(map(int, input().split()))
last[0] -= 1
last[1] -= 1
if first == last:
    print(0)
    print(first[0] + 1, first[1] + 1)
    exit()
p = [[-1 for _ in range(n)] for _ in range(n)]
used = [[0 for _ in range(n)] for _ in range(n)]
used[first[0]][first[1]] = 1
q = [first]
while len(q) != 0:
    v = q[0]
    del q[0]
    # do_and_check_steps()
    if v[0] >= 2 and v[1] >= 1 and used[v[0]-2][v[1]-1] == 0:
        p[v[0]-2][v[1]-1] = v
        used[v[0]-2][v[1]-1] = 1
        q.append([v[0]-2, v[1]-1])
    if v[0] >= 2 and v[1] <= n-2 and used[v[0]-2][v[1]+1] == 0:
        p[v[0]-2][v[1]+1] = v
        used[v[0]-2][v[1]+1] = 1
        q.append([v[0]-2, v[1]+1])
    if v[0] >= 1 and v[1] <= n-3 and used[v[0]-1][v[1]+2] == 0:
        p[v[0]-1][v[1]+2] = v
        used[v[0]-1][v[1]+2] = 1
        q.append([v[0]-1, v[1]+2])
    if v[0] >= 1 and v[1] >= 2 and used[v[0]-1][v[1]-1] == 0:
        p[v[0]-1][v[1]-2] = v
        used[v[0]-1][v[1]-1] = 1
        q.append([v[0]-1, v[1]-2])
    if v[0] <= n-3 and v[1] <= n-2 and used[v[0]+2][v[1]+1] == 0:
        p[v[0]+2][v[1]+1] = v
        used[v[0]+2][v[1]+1] = 1
        q.append([v[0]+2, v[1]+1])
    if v[0] <= n-3 and v[1] >= 1 and used[v[0]+2][v[1]-1] == 0:
        p[v[0]+2][v[1]-1] = v
        used[v[0]+2][v[1]-1] = 1
        q.append([v[0]+2, v[1]-1])
    if v[0] <= n-2 and v[1] >= 2 and used[v[0]+1][v[1]-2] == 0:
        p[v[0]+1][v[1]-2] = v
        used[v[0]+1][v[1]-2] = 1
        q.append([v[0]+1, v[1]-2])
    if v[0] <= n-2 and v[1] <= n-3 and used[v[0]+1][v[1]+2] == 0:
        p[v[0]+1][v[1]+2] = v
        used[v[0]+1][v[1]+2] = 1
        q.append([v[0]+1, v[1]+2])
for i in range(n):
    print(p[i])
steps = []
now = last
steps.append(now)
while p[now[0]][now[1]] != -1:
    now = p[now[0]][now[1]]
    steps.append(now)
print(len(steps)-1)

