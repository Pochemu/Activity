import math
f = open('../../../В процессе/26-s1.txt')
n = f.readline()
prices = []
sale = []
cnt = 0
for i in range(int(n)):
    price = int(f.readline())
    if price > 100:
        sale.append(price)
    else:
        prices.append(price)
sale.sort()
for i in range(len(sale)//2):
    sale[i] = sale[i] * 0.9
print(math.ceil(sum(sale)) + sum(prices), int(sale[len(sale)//2-1]/0.9))