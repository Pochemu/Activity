def dfs(s, table):
    global cnt
    global n
    global used
    used[s] = 1
    cnt += 1
    for i in range(n):
        if table[s][i] == 1 and used[i] == 0:
            dfs(i, table)

n, s = map(int, input().split())
table = [[] for _ in range(n)]
for i in range(n):
    table[i] = list(map(int, input().split()))
used = [0] * n
s -= 1
cnt = 0
dfs(s, table)
print(cnt)