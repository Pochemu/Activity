f = open('test.txt')
place = [[] for _ in range(100)]
n = int(f.readline())
for _ in range(n):
    m, p = map(int, f.readline().split())
    place[m].append(p)
for j in range(100-1, -1, -1):
    place[j].sort()
    for i in range(1, len(place[j])):
        if place[j][i] - place[j][i-1] == 3:
            print(j+1, place[j][i-1]+1)
