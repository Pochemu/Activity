n, m = list(map(int, input().split()))
matrix = [0] * n
for i in range(n):
    matrix[i] = list(map(int, input().split()))
for i in range(1, n):
    matrix[i][0] = matrix[i][0] + matrix[i-1][0]
for i in range(1, m):
    matrix[0][i] = matrix[0][i] + matrix[0][i-1]
for i in range(1,n):
    for j in range(1,m):
        matrix[i][j] = matrix[i][j] + min(matrix[i-1][j],matrix[i][j-1])
print(matrix[n-1][m-1])