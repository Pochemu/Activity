for x in range(101, 1000):
    L = x-30
    M = x+30
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M == 30:
        print(x)
        break