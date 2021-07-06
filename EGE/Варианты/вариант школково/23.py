for i in range(1, 100000):
    x = i
    D = 0
    V = 0
    while x > 0:
        D += 1
        if V < x:
            V = x%10
        x = x//10
    if D == 3 and V == 7:
        print(i)