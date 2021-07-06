a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = []
for x in range(0, 1001):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        s.append(str(x))
print(" ".join(s))
