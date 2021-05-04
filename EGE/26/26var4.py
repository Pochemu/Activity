f = open('../../../В процессе/26-j4.txt')
n = int(f.readline())
files = []
for i in range(n):
    files.append(int(f.readline()))
files.sort()
answer_file = files[n - n//10 - 1]
print(sum(files[n//10:n-n//10]), answer_file)