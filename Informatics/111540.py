def dfs(s, table):
    global cnt, n, used

cnt = 0
n, m = map(int, input().split())
table = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    table[i][j] = 1
    table[j][i] = 1
used = [0] * n
last_used = [1] * n
while used != last_used:
    dfs()

