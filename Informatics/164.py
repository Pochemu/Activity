n, s = map(int, input().split())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
answer = matrix[s-1].count(1) + 1
print(answer)