def decorator(func):
    return func


@decorator  # decorated = decorator(decorated)
def decorated():
    print('Hello')


decorated()


# другой пример


def decorator(func):
    def new_func():
        pass
    return new_func


@decorator
def decorated():
    print('Hello')


decorated()  # внутри декоратора у нас не будет выполнятся функция func, только функция new_func
print(decorated.__name__)


