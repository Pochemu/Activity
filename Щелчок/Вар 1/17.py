cnt = 0
for i in range(444157, 926640):
    if i%6 == 0 and i%31 and i%43 and i%29 and i%19:
        cnt += 1
        max_n = i
print(cnt, max_n)