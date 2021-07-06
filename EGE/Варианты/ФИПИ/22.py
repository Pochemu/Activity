x = int(input())
L = 0
M = 0
while x > 0:
    M = M + 1
    if x % 2 != 0:
        L = L + 1
    x = x // 2
print(L)
print(M)