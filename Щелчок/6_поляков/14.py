n = 9 ** 7 + 3 ** 21 - 8
x = ''
while n > 0:
    x += str(n%3)
    n //= 3
print(sum(map(int, x)))