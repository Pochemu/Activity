range_list = list(range(10))
print(range_list[:] is range_list)  # False
print(range_list[:] == range_list)  # True
print(range_list)
print(range_list[1:3])
print(range_list[3:])
print(range_list[:5])
print(range_list[::2])
print(range_list[::-1])
print(range_list[1:2])
print(range_list[5:1:-1])
