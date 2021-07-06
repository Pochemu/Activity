f = open('test.txt')
n = int(f.readline())
k = [0] * 3
ans = 0
for _ in range(n):
    x = int(f.readline())
    # k_new = k.copy()
    r = x%3
    if r == 0:
        ans += k[0]
        k[0] += 1
        ans += k[0]
    elif r == 1:
        ans += k[2]
        k[1] += 1
        k[0] += k[2]
    else:
        ans += k[1]
        k[2] += 1
        k[0] += k[1]
    # if r != 0:
    #     for i in range(1, 3):
    #         r1 = (r+i)%3
    #         k_new[r1] += k_new[i]
    #     k_new[r] += k[0] + 1
    # else:
    #     for i in range(1, 3):
    #         r1 = r+i
    #         k_new[r1] += k_new[r1]
    #     k_new[0] += k[0] + 1
    # k = k_new.copy()
print(k[0])