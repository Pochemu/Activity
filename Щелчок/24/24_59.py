f = open('shkolkovo_9.txt')
cnt = 3
s_def = 'DEF'
for s in f:
    while True:
        if s_def in s:
            cnt += 1
            s_def += s_def[-3]
        else:
            break
print(len(s_def)-1)