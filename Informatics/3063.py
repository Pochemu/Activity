x = int(input())
p = int(input())
y = int(input())
years = 0
while x < y:
    x = int((x*(1+p/100))*100)/100
    years += 1
print(years)