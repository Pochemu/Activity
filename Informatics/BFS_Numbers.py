first = int(input())
last = int(input())
p = [-1] * 10000
used = [0] * 10000
q = [first]
used[first] = 1
while len(q) != 0:
    v = q[0]
    del q[0]

    if v // 1000 != 9 and used[v+1000] == 0:
        p[v+1000] = v
        used[v+1000] = 1
        q.append(v+1000)

    if v%10 != 1 and used[v-1] == 0:
        p[v-1] = v
        used[v-1] = 1
        q.append(v-1)

    if used[v//10+v%10*1000] == 0:
        p[v//10+v%10*1000] = v
        used[v//10+v%10*1000] = 1
        q.append(v//10+v%10*1000)

    if used[v%1000*10+v//1000] == 0:
        p[v%1000*10+v//1000] = v
        used[v%1000*10+v//1000] = 1
        q.append(v%1000*10+v//1000)

now = last
steps = [now]
while p[now] != -1:
    steps.append(p[now])
    now = p[now]
for i in steps[::-1]:
    print(i)