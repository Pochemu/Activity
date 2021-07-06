f = open('shkolkovo_2.txt')
cnt = 0
cnt_max = 0
for s in f:
    if s.count('A') < 25:
        for i in range(ord('A'), ord('Z')+1):
           cnt = s.rindex(chr(i)) - s.index(chr(i))
           cnt_max = max(cnt, cnt_max)
print(cnt_max)