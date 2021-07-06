# Имеется набор данных, состоящий из положительных целых чисел.
# Необходимо определить количество пар элементов (ai, aj) этого набора,
# в которых 1 <= i + 5 <= j <= N, сумма элементов нечётна, а произведение делится на 13.
f = open('27-17b.txt')
n = int(f.readline())
even_13 = 0
odd_13 = 0
even = 0
odd = 0
ans = 0
buf = []
for _ in range(5):
    x = int(f.readline())
    buf.append(x)
for _ in range(5, n):
    d = buf[0]
    if d%13 == 0:
        if d%2 == 0:
            even_13 += 1
        else:
            odd_13 += 1
    else:
        if d%2 == 0:
            even += 1
        else:
            odd += 1
    x = int(f.readline())
    if x%13 == 0:
        if x%2 == 0:
            ans += odd_13 + odd
        else:
            ans += even_13 + even
    else:
        if x%2 == 0:
            ans += odd_13
        else:
            ans += even_13
    buf.append(x)
    del buf[0]
print(ans)