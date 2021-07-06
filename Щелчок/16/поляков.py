def f(n):
    if n <= 18:
        return n+3
    elif n%3:
        return f(n-1) + n*n + 5
    else:
        return (n//3) * f(n//3) + n -12


cnt = 0
for i in range(1, 801):
    flag = True
    for j in range(1, 10, 2):
        if str(j) in str(f(i)):
            flag = False
    if flag:
        cnt += 1
print(cnt)