def f(n):
    if n == 0:
        return 0
    if n > 0 and n%2 == 0:
        return f(n//2)
    if n%2:
        return 1 + f(n-1)


cnt = 0
for i in range(1, 500):
    if f(i) == 3:
        cnt += 1
print(cnt)