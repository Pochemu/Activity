f = open('18.txt')
num = []
for _ in range(2000):
    x = float(f.readline())
    num.append(x)
sum_max = 0
for i in range(2000):
    s = num[i]
    if (s > sum_max):
        sum_max = s
    for j in range(i+1, 2000):
        if abs(num[j] - num[j-1]) <= 4:
            s += num[j]
            if s > sum_max:
                sum_max = s
        else:
            break
print(sum_max)