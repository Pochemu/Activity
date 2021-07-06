f = open('26.txt')
n = int(f.readline())
num = []
num_n = []
num_c = []
cnt = 0
max_sum = 0
for _ in range(n):
    num.append(int(f.readline()))
for i in num:
    if i%2:
        num_n.append(i)
    else:
        num_c.append(i)
for i in num_n:
    for j in num_c:
        if i+j < 1000000000:
            if i + j in num_n:
                print(i+j)
                max_sum = max(max_sum, i+j)
                cnt += 1
print(cnt)
print(max_sum)