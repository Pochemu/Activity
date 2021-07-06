a = int(input())
b = int(input())
if a == 0 and b == 0:
    print("INF")
elif a == 0 or b % a != 0:
    print("NO")
else:
    print(-b // a)
