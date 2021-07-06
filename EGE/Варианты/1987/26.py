f = open('26-k1.txt')
n, k = map(int, f.readline().split())
costs = []
for _ in range(n):
    costs.append(int(f.readline()))
costs.sort(reverse=True)
print(costs[k], sum(costs[0:k])*0.2)