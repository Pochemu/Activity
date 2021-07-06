for i in range(2, 150):
    x = bin(i)
    x = x[3:].replace('1', '2')
    x = x[3:].replace('0', '1')
    x = x[3:].replace('2', '0')
    x = x[2].replace('0', '1')
    print(str(bin(i))[2:])
    print(x[2:])