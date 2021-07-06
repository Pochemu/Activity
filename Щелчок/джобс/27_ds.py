# На вход программы поступает последовательность из целых положительных
# чисел. Необходимо выбрать такую подпоследовательность подряд идущих
# чисел, чтобы их сумма была максимальной и делилась на 50, а также её
# длину. Если таких подпоследовательностей несколько, выбрать такую, у
# которой длина меньше.
f = open('test.txt')
n = int(f.readline())
ost = [10000000000000001] * 50
sum_max = 0
ind = [-1] * 50
s = 0
lm = 0
for i in range(n):
    x = int(f.readline())
    s += x
    d = s%50
    if d == 0:
        sum_max = s
        lm = i+1
    else:
        if sum_max < s - ost[d]:
            sum_max = s - ost[d]
            lm = i - ind[d]
        if sum_max == s - ost[d]:
            lm = min(lm, i - ind[d])
    if ost[d] > s:
        ost[d] = s
        ind[d] = i
print(sum_max, lm)


