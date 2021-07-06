f = open('24-j5.txt')
for s in f:
    x = s
print(x.count('STOCK'))
print(x.count('OCK') - x.count('STOCK'))