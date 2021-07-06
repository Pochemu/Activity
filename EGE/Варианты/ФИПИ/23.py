list = [0] * 29
list[23] = 1
for i in range(23, 1, -1):
    list[i] += list[i+2] + list[i+5]
    print(i, list[i])
print(list)
