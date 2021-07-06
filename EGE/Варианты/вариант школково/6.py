k = int(input())
n = 14
s = 121
while 2*n + s < 321:
    n = n+k
    s = s-3
print(s)