def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print(list(fibonacci(10)))
for num in fibonacci(10):
    print(num)
