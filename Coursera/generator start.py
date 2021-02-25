def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


ranger = even_range(0, 4)
print(next(ranger))
print(next(ranger))
# print(next(ranger)) Stop iteration
