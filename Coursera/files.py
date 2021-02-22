f = open('just_a_file.txt', 'a')
f.write('Hello \n')
f.close()
with open('just_a_file.txt') as f:
    print(f.read())