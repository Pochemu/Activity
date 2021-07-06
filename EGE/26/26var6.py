line = 0
cnt = 0
file = open('26-j2.txt')
for n in file:
    if line == 0:
        length = int(n)
        numbers = [0] * length
    else:
        numbers[line-1] = int(n)
    line += 1
numbers.sort()
i = length//2 + 1
medium = numbers[i]
average = sum(numbers)/length
while numbers[i] > average:
    cnt += 1
    i -= 1
print(length, i, medium, average)
print(cnt)