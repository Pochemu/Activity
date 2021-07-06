f = open('test.txt')
n = int(f.readline())
max_len = 1
pk1, pk2 = map(int, f.readline().split())
len = 1
for _ in range(n):
    k1, k2 = map(int, f.readline().split())
    if k1 == pk1 or k1 == pk2:

    elif k2 == pk1 or k2 == pk2:

    else:
        max_len = max(max_len, len)
        len = 1