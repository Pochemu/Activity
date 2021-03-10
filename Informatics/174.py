n = int(input())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            cnt += 1
print(cnt//2)