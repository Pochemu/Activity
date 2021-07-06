h = int(input())
a = int(input())
b = int(input())
min_x = (h - a)//(a-b)
x = min_x * (a-b) + a == h
y = (min_x * (a-b) + a + a > h) * x == 0
ans = min_x + 1 * x + 2 * y
print(ans)