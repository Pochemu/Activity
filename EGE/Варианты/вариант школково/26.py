f = open('26.txt')
n, k, m = map(int, f.readline().split())
students = []
for _ in range(n):
    students.append(int(f.readline()))
students.sort(reverse=True)
print(students)
print(students[0:k])
print(students[k-1], students[k])