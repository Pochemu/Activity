n = int(input())
k = int(input())  # в каком столбце максимальная сумма чисел
#---------------------------- вывод суммы
x = 0
i = 0
while x != n:
    i = i + (1 + n * (k-1)) + ((n + 1 - k) * x)
    x += 1
print(i)
# #---------------------------- вывод таблицы
# # z = 1  # какое число выводится
# # x1 = [list(map(int, input().split())) for i in range(n)]
# # y1 = 1 # какой столбец таблицы
# # g = 0
# # # while z <= n*n:
# # #     if y1 <= n:
# # #         print(x1,z)
# # #         z += 1
# # #         y1 += 1
# # #         if y1 != k:
# # #             x1 += 1 + n*g
# # #         else:
# # #             x1 = 1 + n * (k-1) + (n+1-k)*g
# # #     else:
# # #         y1 = 1
# # #         g = g + 1
# # print(x1)
# x = 1
# y = 1
# A = [ ["1", "2", "3"], ["4", "5", "6"] ]
# print(for i in range (1,5):)
# # x = 1
# # # y = 1
# # # while (x and y) <= n:
# # #     print x