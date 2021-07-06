for i in range(100, 1000):
    n1 = i//100
    n2 = (i//10) % 10
    n3 = i % 10
    max_n = max(n1, n2, n3)
    min_n = min(n1, n2, n3)
    sr_n = n1 + n2 + n3 - max_n - min_n
    d_max = max_n * 10 + sr_n
    if min_n != 0:
        d_min = min_n * 10 + sr_n
    else:
        d_min = sr_n * 10 + min_n
    if d_max - d_min == 20:
        print(i)