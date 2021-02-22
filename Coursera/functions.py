def add(x: int, y: int) -> int:
    return x + y


print(add(10, 2))
print(add('still ', 'works'))


def extender(source_list, extend_list):
    source_list.extend(extend_list)  # является плохим тоном


values = [1, 2, 3]
extender(values, ['four', 'five', 'six'])

print(values)


def say(greeting, name) -> str:
    print('{} {}!'.format(greeting, name))


say('Hello', 'DJ')
say(name='Ted', greeting='Hi')


def greeting(name='it\'s me...'):
    print('Hello, {}'.format(name))


greeting()
greeting('my God')


def append_one(iterable=[]):
    iterable.append(1)

    return iterable


print(append_one([1]))
print(append_one.__defaults__)

print(append_one())
print(append_one())  # проблема

print(append_one.__defaults__)


def function(iterable=None):  # решение
    if iterable is None:
        iterable = []
    iterable.append(1)
    return iterable


print(function())
print(function())


