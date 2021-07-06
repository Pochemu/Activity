cnt = 0
for i in range(33334):
    if (i//10000 != 0 and (i//10000 != i%10 or (i//1000)%10 != (i//10)%10)) == 1 and\
            (i // 10000 != 0 and str(i) != str(i)[4:-1:-1]) == 0:
        print(i)
    # if i // 10000 != 0 and str(i) != str(i)[4:-1:-1]:
    #     cnt += 1
print(cnt)