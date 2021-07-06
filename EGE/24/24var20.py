file = open('../В процессе/24-5.txt', 'r')
f = file.read()
counter = 0
answer = 0
for i in f:
    if i == '(':
        counter += 1
    if counter > answer:
        answer = counter
        print(answer)
    if i == ')':
        counter = 0
print(answer)