f = open('24.txt')
list_s = []
for s in f:
    list_s = s
list_s = list_s.split('XZZY')
max_len = 0
for i in list_s:
    max_len = max(max_len, len(i))
print(max_len)