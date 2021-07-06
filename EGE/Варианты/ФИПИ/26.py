f = open('26.txt')
s, n = map(int, f.readline().split())
files = []
for _ in range(n):
    x = int(f.readline())
    files.append(x)
files.sort()
i = 0
save_files = []
while s >= files[i]:
    save_files.append(files[i])
    s -= files[i]
    i += 1
s += save_files[-1]
del save_files[-1]
for i in range(len(files)-1, -1, -1):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
print(len(save_files), save_files[-1])