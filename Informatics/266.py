x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
result = (x1 *x2 > 0) and (y1 * y2 > 0)
print((result == 1) * 'YES' + (result == 0) * 'NO')
