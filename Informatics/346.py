n = int(input())
count_positive = 0
count_0 = 0
count_negative = 0
for i in range(0, n):
    n = int(input())
    if n > 0:
        count_positive += 1
    elif n == 0:
        count_0 += 1
    else:
        count_negative += 1
print(count_0, count_positive, count_negative)
