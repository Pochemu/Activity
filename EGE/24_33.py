cnt_chains = 0
f = open('../../../В процессе/24data/k7c-1.txt')
s = f.readline()
for i in range(len(s)-2):
    if (s[i] in 'BCD' and s[i+1] in 'BDE' and s[i+2] in 'BCE' and
            s[i+1] != s[i] and s[i+2] != s[i+1]):
        cnt_chains += 1
print(cnt_chains)
