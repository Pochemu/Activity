f = open('24-j5.txt')
cnt = 0
for s in f:
    for i in range(len(s)-5):
        if s[i:i+5] == 'OKTOS':
            cnt += 1
print(cnt)