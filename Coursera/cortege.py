empty_tuple = ()
empty_tuple = tuple()
immutables = (int, str, tuple)
# immutables[0] = float - ошибка
print(immutables)
print(type(empty_tuple))
blink = ([],[])
blink[0].append(12)
print(blink)
print(hash(tuple))

