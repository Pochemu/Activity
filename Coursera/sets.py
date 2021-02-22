odd_set = set()
even_set = set()
frozen = frozenset(['Anna', 'Olaf'])  # неизменяемое множество
print(frozen)
for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(*odd_set)
print(*even_set)

# union_set = odd_set | even_set
union_set = odd_set.union(even_set)
print(union_set)

# intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)
print(intersection_set)

# even_set.add(1)
# difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)
print(difference_set)

# symmetric_difference_set = odd_set ^ even_set
symmetric_difference_set = odd_set.symmetric_difference(even_set)
print(symmetric_difference_set)

even_set.remove(2)
print(even_set)

even_set.pop()
print(even_set)