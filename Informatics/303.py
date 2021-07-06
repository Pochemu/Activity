n = int(input())
if n > 20:
    x = n - n//10 * 10
else:
    x = n
if 21>x>4 or x == 0:
    print(n, 'korov')
elif 5>x>1:
    print(n, 'korovy')
else:
    print(n, 'korova')