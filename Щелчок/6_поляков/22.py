cnt = 0
for i in range(1, 1000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        b = b + (x % 10)
        x = x // 10
    if a == 2 and b == 12:
        cnt += 1
print(cnt)