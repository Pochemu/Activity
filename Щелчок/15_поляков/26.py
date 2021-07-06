f = open('26-18.txt')
s, n = map(int, f.readline().split())
files = []
for _ in range(n):
    x = int(f.readline())
    files.append(x)
files.sort()
save_files = []
for i in range(len(files)):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
s += save_files[-1]
del save_files[-1]
print(s)
for i in range(len(files)-1, -1, -1):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
print(sum(save_files))
print(s)
print(save_files)
print(files)
print(len(save_files), save_files[-1])