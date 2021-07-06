f = open('Задание_24__6mex.txt')
n = ''
max_n = ''
for s in f:
    for i in range(10, 100):
        if i%10 >= i//10:
            if str(i) in s:
                print(i)
