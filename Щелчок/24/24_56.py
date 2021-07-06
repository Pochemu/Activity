f = open('shkolkovo_6.txt')
cnt = []
for s in f:
    for i in range(ord('a'), ord('z')+1):
       cnt.append(s.count(chr(i)))
cnt.sort()
print(cnt[-1] - cnt[0])