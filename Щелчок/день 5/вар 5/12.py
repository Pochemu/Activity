s = '145' * 500
while ('14' in s) or ('555' in s):
    if '14' in s:
        s = s.replace('14', '5', 1)
    else:
        s = s.replace('555', '5', 1)
print(s)