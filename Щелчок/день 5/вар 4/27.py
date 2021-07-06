f = open('Задание_27_B__6mf0.txt')
n = int(f.readline())
min_d7 = 0
min_b300 = 0
min_m300 = 0
min_b300d7 = 0
for _ in range(n):
    x = int(f.readline())
    if x>300:
        if x%7 == 0:
            min_b300d7 += 1
        else:
            min_b300 += 1
    else:
        if x%7 == 0:
            min_d7 += 1
        else:
            min_m300 += 1
print(min_d7 * (min_b300 + min_b300d7) + min_m300*min_b300d7)