f = open('26-j5.txt')
n = int(f.readline())
v = []
cnt = 0
for i in range(n):
    v.append(int(f.readline()))
answer_v = [v[0]]
for i in range(1, n-1):
    values = v[i-1: i+2]
    values.sort()
    answer_v.append(values[1])
answer_v.append(v[n-1])
for i in range(n):
    if v[i] > answer_v[i]:
        cnt += v[i] - answer_v[i]
print(answer_v.count(min(answer_v)), cnt)