ans = set()


def f(n, step):
    global ans
    if step == 10:
        ans.add(n)
    else:
        f(n*2, step + 1)
        f(n*2+1, step + 1)


f(1, 0)
print(ans)