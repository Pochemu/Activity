def F(n):
  print(n, end='')
  if n > 3:
    F(n - 1)
    F(n // 2)


print(F(7))