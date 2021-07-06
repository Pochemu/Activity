for i in range(101, 1000):
    x = i
    L = x - 15
    M = x + 20
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M == 35:
        print(i)