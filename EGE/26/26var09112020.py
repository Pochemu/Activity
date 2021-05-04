costs = []
with open('26.txt') as f:
	n, k, m = map(int, f.readline().split())
	for i in range(n):
		costs.extend(list(map(int, f.readline().splitlines())))
costs.sort()
average_val = sum(costs[0:k])/k
print(costs[-m], round(average_val))
