n = int(input())
number = 2**n-1
for i in range(2**n):
    print((n - len(bin(number)[2::]))*'0'+str(bin(number)[2::]))
    number -= 1
