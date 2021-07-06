n = int(input())  # количество компьютеров у Виталика
coins = list(map(int, input().split()))
get_coins = list(map(int, input().split()))
lost_coins = [0] * n
for i in range(n):
    lost_coins[i] = coins[i] - get_coins[i]
print(lost_coins.index(max(lost_coins))+1)