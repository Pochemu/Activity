f = open('27-16a.txt')
n = int(f.readline())
even_13 = 0
odd_13 = 0
even = 0
odd = 0
ans = 0
for _ in range(n):
    x = int(f.readline())
    if x%13 == 0:
        if x%2 == 0:
            ans += odd_13 + odd
            even_13 += 1
        else:
            ans += even_13 + even
            odd_13 += 1
    else:
        if x%2 == 0:
            ans += odd_13
            even += 1
        else:
            ans += even_13
            odd += 1
print(ans)