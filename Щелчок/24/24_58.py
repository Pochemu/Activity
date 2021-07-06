f = open('shkolkovo_8.txt')
cnt = 0
cnt_max = 0
ans = 100000000
for s in f:
    for i in range(ord('A'), ord('Z')+1):
        cnt = s.count('A'+chr(i))
        if cnt > cnt_max:
            cnt_max = cnt
            ans = min(ans, i)
print(chr(i)+str(cnt_max))