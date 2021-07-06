f = open('27-7b.txt')
n = int(f.readline())
R = 1
max_d7 = 0
max_n7 = 0
for _ in range(n):
    x = int(f.readline())
    if not x%7:
        if x%49:
            max_d7 = max(max_d7, x)
    else:
        max_n7 = max(max_n7, x)
print(max_n7, max_d7)
print(max(max_d7 * max_n7, R))