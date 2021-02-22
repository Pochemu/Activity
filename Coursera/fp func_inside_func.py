def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


multiplier = get_multiplier()
print(multiplier(12, 3))
print(multiplier.__name__)


def get_another_multiplier(number):
    def inner(a):
        return a * number
    return inner


multiplier_by_2 = get_another_multiplier(2)
print(multiplier_by_2(21))
print(multiplier_by_2.__name__)
print(get_another_multiplier(2)(10))