for i in range(10, 65):
    j = i+35
    if i//10 == j//10 or i//10 == j%10 or i%10 == j//10 or i%10 == j%10:
        print(i, j)