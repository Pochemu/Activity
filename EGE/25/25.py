ans = []
for m in range(0, 29, 2):
    if 200_000_000 <= 2**m <= 400_000_000:
        ans.append(2**m)
    for n in range(1, 19, 2):
        if 200_000_000 <= 2 ** m * 3 ** n <= 400_000_000:
            ans.append(2 ** m * 3 ** n)
ans.sort()
for i in ans:
    print(i)