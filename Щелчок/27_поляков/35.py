f = open('27-35b.txt')
n = int(f.readline())
k_odd = 0
k_even = 0
ans = 0
odd = 0
even = 0
for _ in range(n):
    x = int(f.readline())
    if x > 0:
        if x%2 == 0:
            ans += k_even
            even += 1
        else:
            ans += k_odd
            odd += 1
    elif x == 0:
        k_odd += odd
        k_even += even
        odd = 0
        even = 0
print(ans)