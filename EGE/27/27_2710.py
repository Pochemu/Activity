f = open('27-35b.txt')
n = int(f.readline())
odd_work = 0
odd_wait = 0
even_work = 0
even_wait = 0
ans = 0
for _ in range(n):
    x = int(f.readline())
    if x != 0:
        if x % 2 == 0:
            even_wait += 1
            ans += even_work
        else:
            odd_wait += 1
            ans += odd_work
    else:
        even_work += even_wait
        even_wait = 0
        odd_work += odd_wait
        odd_wait = 0
print(ans)