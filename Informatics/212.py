n = int(input())
costs = [0] * n
min_costs = [0] * n
for i in range(n-1, -1, -1):
    costs[i] = list(map(int, input().split()))
min_costs[0] = costs[0][0]
if n > 1:
    min_costs[1] = min(costs[1][0]+min_costs[0], costs[1][1])
if n > 2:
    min_costs[2] = min(costs[2][0]+min_costs[1], costs[2][1] + costs[0][0], costs[2][2])
if n > 3:
    for i in range(3, n):
        min_costs[i] = min(costs[i][0]+min_costs[i-1], costs[i][1] + min_costs[i-2], costs[i][2] + min_costs[i-3])
print(min_costs[n-1])