file = open('24-5 (1).txt', 'r')
f = file.read()
counter = 0
i = 0
while counter != 10000:
    if f[i] == ')':
        counter += 1
    i += 1
print(i)