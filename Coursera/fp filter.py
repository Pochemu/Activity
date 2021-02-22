def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-2, 4))))


def even(a):
    return a % 2 == 0


print(list(filter(even, range(-5, 15))))