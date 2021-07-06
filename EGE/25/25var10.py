for i in range(190201, 190221):
    count_del = 0
    for j in range(1, int(i**0.5)):
        if i % j == 0:
            count_del += 2
            second_answer = i // j
    if (j+1)**2 == i:
        count_del += 1
    if count_del == 4:
        print(i, second_answer)