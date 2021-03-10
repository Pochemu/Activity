cnt = 0
with open('24-5.txt') as f:
    for s in f:
        for i in range(len(s)-1):
            if s[i:i+2] == '()':
                cnt += 1
            if cnt == 10000:
                print(i+1)