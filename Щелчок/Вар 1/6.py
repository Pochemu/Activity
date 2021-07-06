for i in range(1, 100000):
    k = i
    n = 1392
    s = -185
    while n > s:
        n = n - k *5
        s = s+n//10
    if s == 1:
        print(i)
print(2**12)