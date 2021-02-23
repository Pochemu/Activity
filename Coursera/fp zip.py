num_list = range(7)
squared_list = [x ** 2 for x in num_list]

print(list(zip(num_list, squared_list)))
print(list(zip(filter(bool, range(3)), [x for x in range(3) if x])))
