r =[0]*11
r[3] = 1
for i in range(3, 11):
    r[i] += r[i-1] + r[i-2] + r[i//2]
print(r[10])
print(r)