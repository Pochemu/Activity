n, max_m = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))
m.insert(0, 0)
c.insert(0, 0)
values = [[0 for _ in range(max_m+1)]for _ in range(n+1)]
items = [[[] for _ in range(max_m+1)]for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, max_m+1):
        if m[i] <= j:
            if values[i-1][j] > values[i-1][j - m[i]] + c[i]:
                values[i][j] = values[i-1][j]
                items[i][j].extend(items[i-1][j])
            else:
                values[i][j] = values[i-1][j - m[i]] + c[i]
                items[i][j] = items[i-1][j - m[i]] + [i]
        else:
            values[i][j] = values[i-1][j]
            items[i][j].extend(items[i-1][j])
answer = items[i][j]
for i in range(len(answer)):
    print(answer[i])