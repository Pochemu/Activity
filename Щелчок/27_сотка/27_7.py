f = open('27A.txt')
n = int(f.readline())
num = []
ans =  10001
s_ans = 0
for _ in range(n):
    x = int(f.readline())
    num.append(x)
for i in range(n-3):
    for j in range(i+3, n):
        if (num[i] + num[j])%11 == 0:
            ans = min(ans, (num[i] + num[j]))
            s_ans += num[i] + num[j]
print(ans, s_ans)