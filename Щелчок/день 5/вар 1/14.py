n = 15**19 + 15**9 - 322
x = ''
while n > 0:
    x = x + str(n%15)
    n //= 15
print(x)