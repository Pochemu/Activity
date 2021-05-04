f = open('../../../В процессе/24data/24-1.txt')
s = f.readline()
cnt, cnt_max = 0, 0
answer = []
number = []
for i in range(len(s)-2):
    if s[i].isdigit():
        if int(s[i])%2 == 0 and s[i-1].isdigit():
            if int(s[i-1]) == 0:
                cnt = 1
                number.append(int(s[i-1]))
        if int(s[i])%2 == 0 and s[i+1].isdigit():
            if int(s[i+1]) % 2 == 0:
                cnt += 1
                number.append(int(s[i]))
                if cnt_max < cnt:
                    cnt_max = cnt
                    answer = number
        else:
            cnt = 0
            number = []
print(str(answer)[1:len(answer)*3-1:3])