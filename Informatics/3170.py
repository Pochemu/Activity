arrange = list(map(int, input().split()))
counter = 0
for i in range(len(arrange)):
    for j in range(i+1, len(arrange)):
        if arrange[i] == arrange[j]:
            counter += 1
print(counter)