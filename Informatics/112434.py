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
find_max = [0]
index = 0
find_answer = []
answer_index = 0
for i in cnt_sweets.keys():
    find_answer.append(i)
for i in cnt_sweets.values():
    if i > find_max[0]:
        find_max[0] = i
        answer_index = index
    elif i == find_max[0] and find_answer[answer_index] < find_answer[i]:
        find_max[0] = i
        answer_index = index
    index += 1
print(find_answer)
print(find_answer[answer_index])

