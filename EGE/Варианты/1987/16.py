def F(n):
  if n > 1:
    return 2*n + \
           F(n-2)+F(n-3)
  else:
    return n + 5


print(F(6))