n = int(input())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
input()
colors = list(map(int, input().split()))
bad_bridges = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and colors[i] != colors[j]:
            bad_bridges += 1
print(bad_bridges//2)