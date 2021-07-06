f = open('27B.txt')
n = int(f.readline())
b_33 = [0] * 91
m_33 = [0] * 91
ans = 0
for _ in range(n):
    x = int(f.readline())
    if x > 33:
        b_33[x%91] += 1
    else:
        m_33[x % 91] += 1
for i in range(1, 91//2+1):
    ans += b_33[i] * b_33[91-i] + b_33[i] * m_33[91-i] + m_33[i] * b_33[91-i]
if b_33[0] > 1:
    ans += (b_33[0] * (b_33[0] - 1))//2 + b_33[0] * m_33[0]
print(ans)