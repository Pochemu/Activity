import random


numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 10))

print(numbers)

print(reversed(numbers))
print(list(reversed(numbers)))

print(sorted(numbers))
# numbers.sort()
# print(numbers)

print(sorted(numbers, reverse=True))
# numbers.sort(reverse=True)
# print(numbers)