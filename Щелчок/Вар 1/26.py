f = open('26.txt')
n, k, m = map(int, f.readline().split())
files = []
for _ in range(n):
    x = int(f.readline())
    files.append(x)
files.sort(reverse=True)
print(files)
print(files[k+m-1], files[k-1])