n = int(input())
x = 0
net_znach = 1
znach_naid = 0
if len(str(n))%2 == 0:
    while x <= n:
        x += 1
        x_str = str(x)
        if (x + int(x_str[::-1]) == n) & (znach_naid == 0):
            print(x)
            net_znach = 0
            znach_naid = 1
else:
    while x <= n/2:
        x += 1
        x_str = str(x)
        if (x + int(x_str[::-1]) == n) & (znach_naid == 0):
            print(x)
            net_znach = 0
            znach_naid = 1
if net_znach == 1:
    print(0)
