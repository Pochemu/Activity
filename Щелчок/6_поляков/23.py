num = [0] * 16
num[1] = 1
for i in range(2, 16):
    num[i] = num[i-1] + num[i-3] + num[i//3] * (i%3 == 0)
print(num)