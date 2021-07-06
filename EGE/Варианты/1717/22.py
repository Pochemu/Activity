x = 510
L = 0
M = 0
while x > 0:
  M = M + 1
  if x % 2 != 0:
    L = L + x % 8
  x = x // 8
print(L)
print(M)