a = int(input())
b = int(input())
k = int(input())
while k > 0:
    if a <= b:
        b -= 1
        k -= 1
    else:
        a -= 1
        k -= 1
    print(a, b)
print(a, b)
