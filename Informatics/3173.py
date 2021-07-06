array = list(map(int, input().split()))
counter = 0
maximum = 0
for i in set(array):
    for j in range(len(array)):
        if array[j] == i:
            counter += 1
        if counter > maximum:
            maximum = counter
            answer = i
    counter = 0
print(answer)