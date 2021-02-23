"""
не очень
"""
square_list_bad = []
for number in range(10):
    square_list_bad.append(number**2)

print(square_list_bad)


"""
зашибись
"""
square_list_good = [number**2 for number in range(10)]
print(square_list_good)

# ещё примеры

"""
так не стоит
"""

even_list_bad = []
for number in range(10):
    if number % 2 == 0:
        even_list_bad.append(number)


print(even_list_bad)

"""
а вот так хорошо
"""
even_list_good = [num for num in range(10) if num % 2 == 0]
print(even_list_good)

# пример со словарями
square_map = {num: num**2 for num in range(5)}
print(square_map)

# пример со множествами
reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

# а тип такого выражения - генератор
print(type(number ** 2 for number in range(10)))