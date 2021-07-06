f = open('../../../../В процессе/test.txt')
n = int(f.readline())
sum_max = 0
sum_min = 0
n_c_1 = [100001, 100001]
n_c_2 = [100001, 100001]
n_n_1 = [100001, 100001]
n_n_2 = [100001, 100001]
for _ in range(n):
    a, b = map(int, f.readline())
    if a % 2:
        sum_max += max(a, b)
        sum_min += min(a, b)
        if b%2 and b < n_n_1[]