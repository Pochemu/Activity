f = open('26-1.txt')
s, n = map(int, f.readline().split())
files = []
save_files = []
for _ in range(n):
    files.append(int(f.readline()))
files.sort()
i = 0
while files[i] <= s:
    save_files.append(files[i])
    s -= files[i]
    i += 1
s += save_files[-1]
del save_files[-1]
for i in range(len(files)-1, len(save_files), -1):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
print(len(save_files), save_files[-1])