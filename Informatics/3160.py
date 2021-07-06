array = list(map(int, input().split()))
answer = []
for i in set(array):
    if i%2 != 0:
        answer.append(i)
if len(answer) == 0:
    print(0)
else:
    print(min(answer))