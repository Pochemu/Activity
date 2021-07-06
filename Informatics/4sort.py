def find(x, list_find):
    if len(list_find) != 2:
        l = len(list_find)//2
    else:
        l = 0
    if l == 0 or l == 1:
        if x == list_find[l]:
            return 'YES'
        else:
            return 'NO'
    elif x < list_find[l]:
        find(x, list_find[0:l+1])
    elif x > list_find[l]:
        find(x, list_find[l+1:len(list_find)])

n, k = map(int, input().split())
n_num = list(map(int, input().split()))
m_num = list(map(int, input().split()))
for i in m_num:
    print(find(i, n_num))