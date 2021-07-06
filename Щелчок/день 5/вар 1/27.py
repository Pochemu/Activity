f = open('Задание_27_A__6ldo.txt')
n = int(f.readline())
max_n = 0
pmax_n9 = 0
max_n9 = 0
for _ in range(n):
    x = int(f.readline())
    if x%9 == 0:
        if max_n9 <= x:
            pmax_n9 = max_n9
            max_n9 = x
    else:
        max_n = max(max_n, x)
print(max(max_n9 * max_n, pmax_n9 * max_n9))