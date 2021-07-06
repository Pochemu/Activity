n = int(input())
even = 0
odd = 0
for i in range(2, n, 2):
    if n >= i:
        even += 1
for i in range(1, n, 2):
    if n >= i:
        odd += 1
minutes = 540 + n * 45 + 5 * odd + 15 * even
print(minutes // 60, minutes % 60)
