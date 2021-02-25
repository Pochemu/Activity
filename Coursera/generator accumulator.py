def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value


generator = accumulator()
print(next(generator))
print('Accumulated: {}'.format(generator.send(1)))  # send отправляет в строку value = yield total
print('Accumulated: {}'.format(generator.send(3)))
next(generator)