n = [int(s) for s in input().split()]
nod = 1
n_1,n_2 = n[0],n[1]
if n_1 < n_2:
    n_1, n_2 = n_2, n_1
for i in range(1, n_2 + 1):
    if n_1 % i == 0 and n_2 % i == 0:
        nod = i
print(nod)
