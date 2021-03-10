n, m = map(int, input().split())
i = [0 for _ in range(m)]
j = [0 for _ in range(m)]
for k in range(m):
    i[k], j[k] = map(int, input().split())
traffic_lights = [0 for _ in range(n)]
for k in range(m):
    traffic_lights[j[k]-1] += 1
    traffic_lights[i[k]-1] += 1
print(*traffic_lights)