x = 9**22 + 3**66 - 12
n = ''
while x > 0:
    n += str(x%3)
    x //= 3
print(n.count('2'))