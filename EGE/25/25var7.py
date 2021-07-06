for i in range(164700, 164753):
    count_del = 0
    second_del = 0
    for j in range(1, int(i**0.5)):
        if i % j == 0:
            count_del += 2
            if count_del == 4:
                second_del = i//j
    if (j + 1)**2 == i:
        count_del += 1
    if count_del == 6:
        print(second_del, i)



