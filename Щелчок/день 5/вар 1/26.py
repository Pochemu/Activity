f = open('Задание_26__6ldn.txt')
n, k, m = map(int, f.readline().split())
files = []
for _ in range(n):
    x = int(f.readline())
    files.append(x)
files.sort(reverse=True)
print(files[k], files[0])
