for i in range(int(12034679**0.5) + 1, int(23175822**0.5) + 1):
    cnt_del = 1
    for j in range(2, i):
        if i**2 % j == 0:
            cnt_del += 2
            answer = j
    if cnt_del == 3:
        print(i**2, i**2//(answer),)