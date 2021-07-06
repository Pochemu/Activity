n = int(input())
i = 0
for y in range(n + 1):
    for x in range(y):
        print(y)
        i += 1
        if i == n:
            break
    if i == n:
        break
