n, m = map(int, input().split())
str_lst = list(range(0, n))
int_lst = list(range(0, n))
position_lst = list(range(0, n))
for i in range(0, n):
    str_lst[i] = input().split()
    str_lst[i].append("1")  # 1-лягушка может ходить, 0-лягушка пропускает ход
for i in range(0, n):
    int_lst[i] = [int(x) for x in str_lst[i]]
    position_lst[i] = int_lst[i][0]
hod = 1  # условие выхода из цикла
ost = 0  # количество остановившихся лягушек
new_kil = -1
count = 0
def func():
    for y in range(0, i):  # ищет этих лягушек

        if position_lst[y] == x and position_lst[y] != 0:
            position_lst[y] = 0
            int_lst[y][2] = 0
            int_lst[i][1] -= 1
    for y in range(i + 1, n):

        if position_lst[y] == x and position_lst[y] != 0:
            position_lst[y] = 0
            int_lst[y][2] = 0
            int_lst[i][1] -= 1
# print(n,m,str_lst, int_lst, position_lst)
while hod == 1:
    for i in range(0, n):
        if int_lst[i][2] == 1:
            old_position = position_lst[i]
            position_lst[i] += int_lst[i][1]
            if position_lst[i] > m:
                position_lst[i] -= m
                for x in range(old_position, m + 1):  # лягушек на какой позиции эта лягушка перепрыгнула
                    func()
                for x in range(0, position_lst[i] + 1):
                    func()
            else:
                for x in range(old_position, position_lst[i] + 1):  # лягушек на какой позиции эта лягушка перепрыгнула
                    func()
        if position_lst.count(0) + 1 == len(position_lst):
            hod = 0
        if int_lst.count(0) == len(int_lst):
            hod = 0
        kill = position_lst.count(0)
        if kill == new_kil:
            count += 1
        else:
            new_kil = kill
        if count > 1:
            hod = 0

pr = len(position_lst) - position_lst.count(0)
print(pr)
final_lst = list(range(0, pr))
if pr != 1:
    for i in range(0, pr):
        for v in range(0, len(position_lst)):
            if position_lst[v] > 0 and position_lst[v] != m:
                m = position_lst[v]
                final_lst[i] = v + 1
                break
else:
    for i in range(0, pr):
        for v in range(0, len(position_lst)):
            if position_lst[v] > 0:
                m = position_lst[v]
                final_lst[i] = v + 1
                break

print(*final_lst)
