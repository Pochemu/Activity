def caller(func, params):
    return func(*params)


def printer(name, origin):
    print('I\'m {} of {}'.format(name, origin))


caller(printer, ['Moana', 'Motunuil'])