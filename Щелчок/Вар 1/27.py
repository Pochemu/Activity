f = open('Zadanie_27_B__6isb.txt')
n = int(f.readline())
sum_max = 0
d_min = 10001
for _ in range(n):
    a, b = map(int, f.readline().split())
    d = abs(a-b)
    sum_max += max(a, b)
    if d%3:
        d_min = min(d_min, d)
if sum_max%3 == 0:
    print(sum_max+d_min)
else:
    print(sum_max)