answer = 0
sum_numbers = 0


def function(n):
    if n > 25:
        n = n**2 + 4*n + 3
    elif n % 3 == 0:
        n = function(n+1) + 2*function(n+4)
    else:
        n = function(n+2) + 3*function(n+5)
    return (n)


for i in range(1, 1001):
    for j in str(function(i)):
        sum_numbers += int(j)
    answer += 1 if sum_numbers == 24 else 0
    print(i, function(i), sum_numbers, answer)
    sum_numbers = 0
print(answer)