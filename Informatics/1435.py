ip = list(map(str, input().split('.')))
for i in ip:
    if i.isdigit():
        if 256 > int(i) >= 0:
            pass
        else:
            exit(print(0))
    else:
        exit(print(0))
print(1)
