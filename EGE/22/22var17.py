x = 117
L = x - 18
M = x + 36
while L != M:
  if L > M:
    L = L - M
  else:
    M = M - L
print(M)