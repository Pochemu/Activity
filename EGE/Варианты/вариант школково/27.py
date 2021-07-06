f = open('27b.txt')
n = int(f.readline())
max_n1 = 0
max_n2 = 0
for _ in range(n):
    x = int(f.readline())
    if x%5 != 0:
        if x > max_n1:
            max_n2 = max_n1
            max_n1 = x
        elif x > max_n2:
            max_n2 = x
print(max_n1 * max_n2)