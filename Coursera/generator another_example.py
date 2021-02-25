def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding: {}'.format(item))


generator = list_generator([1, 2])
print(next(generator))
print(next(generator))