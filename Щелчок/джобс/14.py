n = 4 * 625 ** 9 - 25**15 + 2 * 5 ** 11 - 7
n5 = ''
while n > 0:
    n5 += str(n%5)
    n //= 5
print(n5.count('4'))