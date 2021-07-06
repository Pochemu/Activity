numbers = list(map(int, input().split()))
s = numbers[0]  # количество рублей, которое дала Пете мама
n = numbers[1]  # минимальное количество шариков
k = numbers[2]  # максимальное количество ирисок
a = numbers[3]  # стоимость одного шарика
b = numbers[4]  # стоимость одной ириски
change = s - n*a
answer_sweets = change//b
if answer_sweets > k:
    answer_sweets = k
change = change - answer_sweets * b
answer_baloons = n + change//a
print(answer_baloons, answer_sweets)