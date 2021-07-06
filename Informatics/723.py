string = input()
end_index = -2 if len(string) % 2 != 0 else -3
print(string[0:-1:2] + string[end_index::-2])
