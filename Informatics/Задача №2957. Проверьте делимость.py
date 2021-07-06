n = int(input())
m = int(input())
answer = [m - n * (m//n)+1,n - m*(n//m)+1]
answer.sort()
print(answer[0])
