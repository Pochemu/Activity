x = 9
a = 3*x + 23
b = 3*x - 17
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)