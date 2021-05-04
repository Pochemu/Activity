maximum = 0
cnt = 0
for i in range(4096, 15625):
    number = i
    hex_number = []
    while number != 0:
        hex_number.append(number % 16)
        number //= 16
    if hex_number[0] == 10 and hex_number[1] == 15:
        cnt += 1
        maximum = i
print(cnt, maximum)
print(hex(maximum))