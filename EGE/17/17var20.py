answer = []
for i in range(2595, 8402):
    if i%2 == 0 and i%13 != 0:
        answer.append(i)
print(len(answer), sum(answer))