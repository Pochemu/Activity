import math
f = open('18.txt')
num = []
max_sum = 0
for _ in range(500):
    x = float(f.readline())
    num.append(x)
flag = False
sum_n = []
for i in range(1, 499):
    if abs(num[i] - num[i+1]) <= 5:
        sum_n.append(num[i])
    elif abs(num[i] - num[i-1]) <= 5:
        sum_n.append(num[i])
        max_sum = max(max_sum, sum(sum_n))
        sum_n = []
print(math.floor(max_sum))