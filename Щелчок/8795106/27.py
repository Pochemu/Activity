f = open('27986_B.txt')
x = int(f.readline())
d_max = 0
d_max7 = 0
while x != 0:
    if x%7 == 0 and x%49 != 0:
        d_max7 = max(d_max7, x)
    elif x%49 != 0:
        d_max = max(d_max, x)
    x = int(f.readline())
else:
    print(d_max * d_max7)