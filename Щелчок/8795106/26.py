f = open('28132.txt')
s, n = map(int, f.readline().split())
files = []
for _ in range(n):
    x = int(f.readline())
    files.append(x)
files.sort()
save_files = []
for i in range(n):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
print(len(save_files), save_files[-1])