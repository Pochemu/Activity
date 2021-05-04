files = []
save_files = []
with open('26-17.txt') as f:
    s, n = list(map(int, f.readline().split()))
    for i in range(n):
        files.extend(f.readline().splitlines())
    for i in range(n):
        files[i] = int(files[i])
files.sort()
print(s)
for i in range(n):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
        files[i] = '-'
print(save_files)
for i in range(s, -1, -1):
    if save_files[-1] + i in files:
        save_files[-1] += i
        break
print(len(save_files), save_files[-1])
print(save_files)