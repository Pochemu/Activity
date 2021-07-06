string = 'X' * 49
while ('XXX' in string) or ('ZYX' in string) or ('ZXX' in string):
    string = string.replace('ZYX', 'X', 1)
    string = string.replace('XXX', 'ZZ', 1)
    string = string.replace('ZXX', 'Y', 1)
print(string)
