for i in range(251811, 251827):
    count_del = 0
    answer = 0
    for j in range (1, int(i**0.5)):
        if i%j == 0:
            count_del += 2
            answer = j
    if (j+1)**2 == i:
        count_del += 1
    if count_del == 4:
        print(i//answer, i)