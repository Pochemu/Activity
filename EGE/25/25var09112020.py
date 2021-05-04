simple_n = []
for i in range(1, 1000):
    is_sim = 1
    for j in range(2, i):
        if i % j == 0:
            is_sim = 0
    if is_sim == 1:
        simple_n.append(i)
del simple_n[0]
simple_n.reverse()
for i in range(485617, 529679):
    number = i
    num_del = []
    for k in simple_n:
        if number % k == 0:
            num_del.append(k)
            number //= k
    if len(num_del) == 3 and number == 1:
        if num_del[0] - num_del[2] < 100:
            if num_del[0] % 10 == num_del[1] % 10 == num_del[2] % 10:
                print(i)
