N_10 = int(input())
i = 1
N_2 = 0
answer = ''
while N_10 > 0:
    N_2 = (N_10 % 2) ** i
    N_10 //= 2
    i += 1
    answer = answer + str(N_2)
print(answer)
