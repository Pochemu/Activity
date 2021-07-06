counter = 0
num = 0
for i in range(7849,2476, - 1):
    if i%2 == 0 and i%5 != 0 and i%8 != 0 and i%9 != 0 and i%13 != 0:
        counter += 1
        num = i
print(counter, num)