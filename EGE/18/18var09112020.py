with open('18.txt') as f:
    numbers = []
    for _ in range(300):
        numbers.append(int(f.readline()))
cnt = 0
cnt_max = 0
for i in numbers:
    if i%2:
        cnt += 1
        cnt_max = max(cnt, cnt_max)
    else:
        cnt = 0
print(cnt_max)