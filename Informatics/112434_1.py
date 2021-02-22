n = int(input())
cnt_sweets = {}
for i in range(n):
    d, k = list(map(int, input().split()))
    sweets = k % d
    if sweets in cnt_sweets:
        cnt_sweets[sweets] += 1
    else:
        cnt_sweets[sweets] = 1
if 0 in cnt_sweets:
    del cnt_sweets[0]
keys_answer = []
values_answer = []
answer = {}
for i in cnt_sweets.keys():
    keys_answer.append(i)
for i in cnt_sweets.values():
    values_answer.append(i)
for i in range(len(values_answer)):
    answer[values_answer[i]] = []
for i in range(len(values_answer)):
    answer[values_answer[i]].append(keys_answer[i])
try:
    print(max(answer[max(answer)]))
except ValueError:
    print(0)