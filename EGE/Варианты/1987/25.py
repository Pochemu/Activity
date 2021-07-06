print(525784203**0.5)
print(728943762**0.5)
for i in range(22930, 26999):
    cnt_del = 0
    d = 0
    number = i**2
    for j in range(2, i):
        if number % j == 0:
            cnt_del += 2
            d = j
    if cnt_del == 2:
        print(i**2, d, number//d)