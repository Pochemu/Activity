a = str(input())
b = str(input())
i = 0
x = (a.rpartition(b))
while(str(x[1])) == b:
    i += 1
    a = x[0]
    x = (a.rpartition(b))
print(i)