f = open('Задание_26__6mez.txt')
files = []
s, n = map(int, f.readline().split())
for _ in range(n):
    files.append(int(f.readline()))
files.sort()
save_files = []
for i in range(n):
    if files[i] <= s:
        save_files.append(files[i])
        s -= files[i]
print(len(save_files), save_files[0])