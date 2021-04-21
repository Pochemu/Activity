n = int(input())
matrix = [0 for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
ways = []
len_ways = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != 0:
#             for k in range(n):
#                 if matrix[j][k] != 0 and k != i:
#                     ways.append([i+1, j+1, k+1])
#                     len_ways.append(matrix[i][j] + matrix[j][k] + matrix[k][1])
# print(*ways[len_ways.index(min(len_ways))])
for i in range(n):
    for j in range(n):
        if i!= j:
            for k in range(n):
                if j!=k and k != i:
                    ways.append([i+1, j+1, k+1])
                    len_ways.append(matrix[i][j] + matrix[j][k] + matrix[k][1])
print(*ways[len_ways.index(min(len_ways))])