from functools import reduce


def multiply(a, b):
    return a * b


print(reduce(multiply, [1, 2, 3, 4, 5]))


print(reduce(lambda x, y: x * y, range(1, 6)))
