n, m = list(map(int, input().split()))
matrix = [[0 for x in range(n)] for y in range(m)]
matrix[0] = [1]*n
for i in range(m):
    matrix[i][0] = 1
for i in range(1,m):
    for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
print(matrix[m-1][n-1])