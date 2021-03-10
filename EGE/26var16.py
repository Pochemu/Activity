files = []
save_files = []
with open('26-17.txt') as f:
    s, n = map(int, f.readline().split())
    for i in range(n):
        files.extend(map(int, f.readline().splitlines()))
files.sort()
for i in range(n):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
        files[i] = '-'
    else:
        while save_files[-1] + s not in files:
            s -= 1
        else:
            save_files[-1] += s
            s = 0
            break
print(len(save_files), save_files[-1])