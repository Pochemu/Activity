f = open('Задание_27_A__6mfa.txt')
n = int(f.readline())
z = [0] * 3
max_s = 0
d1 = 0
d2 = 0
for _ in range(n):
    a, b, c = map(int, f.readline().split())
    z[0] = a
    z[1] = b
    z[2] = c
    z.sort()
    max_s += z[2]
    d1 += z[0]
    d2 += z[1]
print(d1, d2, max_s)
