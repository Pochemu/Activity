n = int(input())
numbers = list(map(int, input().split()))
answer = []
for i in range(0, n, 2):
    answer.append(numbers[i])
print(*answer)  # офигеть просто, я думал там жесть какая-та будет а тут просто распаковка, я в шоке!!!
