s = '4' * 207
while '4444' in s or '555' in s:
    if '4444' in s:
        s = s.replace('4444', '5', 1)
    else:
        s = s.replace('555', '44', 1)
print(s)