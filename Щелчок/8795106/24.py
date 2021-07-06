f = open('zadanie24_2.txt')
s_l = 'L'
for s in f:
    while s_l in s:
        s_l += 'L'
print(len(s_l)-1)