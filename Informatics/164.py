def dfs(v):
    global adjustment_matrix
    global cnt
    used[v] = 1
    cnt += 1
    for i in range(n):
        if adjustment_matrix[v][i] == 1 and used[i] == 0:
            dfs(i)


n, s = map(int, input().split())
adjustment_matrix = [[] for _ in range(n)]
used = [0] * n
s -= 1
cnt = 0
for i in range(n):
    adjustment_matrix[i] = list(map(int, input().split()))
dfs(s)
print(cnt)