cnt = 0
for i in range(1, 10000):
    n = i
    if not(n % 2):
        n = n//2
    else:
        n = n - 1
    if not(n % 3):
        n = n //3
    else:
        n = n-1
    if not(n % 7):
        n = n //7
    else:
        n = n-1
    if n == 1:
        print(i)
        cnt += 1
print(cnt)