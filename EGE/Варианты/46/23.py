def F(n):
    global cnt
    if n == 18:
        cnt += 1
    elif n < 18:
        F(n+1)
        F(n*2)
        F(n*3)


cnt = 0
for n in range(1, 23):
    F(n)
print(cnt)