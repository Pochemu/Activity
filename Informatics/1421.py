string = input()
print(' '.join(string.split()))
if string[0] == ' ':
    print(' ' + ' '.join(string.split()))
else:
    print(' '.join(string.split()))
