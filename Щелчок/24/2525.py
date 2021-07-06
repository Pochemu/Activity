f = open('24-1.txt')
max_n = 0
n = ''
for s in f:
    string = s
for i in range(int(ord('A')), int(ord('Z'))+1):
    string = string.replace(chr(i), ' ')
s = string.split()
max_n  = 0
for i in s:
    if int(i)%2 == 0:
        max_n = max(max_n, int(i))
print(max_n)
print(help(str))