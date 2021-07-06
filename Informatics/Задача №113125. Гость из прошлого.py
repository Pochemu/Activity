n = float(input())
a = float(input())
b = float(input())
c = float(input())
i1 = 0
while n >= b:
    n = n - b + c
    i1 += 1
i2 = (n - n % a) // a
if i1> i2:
    print(int(i1))
else:
    print(int(i2))
