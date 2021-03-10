R = [0 for _ in range(15)]
R[0] = 1
for i in range(1, 9):
    R[i] = R[i-1] + R[i-3]
for i in range(8, 15):
    R[i] = R[i-1]
    if i > 9:
        R[i] += R[i-3]
print(R, len(R))
