#11648
N = int(input())
cnt = 0

while N >= 10:
    temp = 1
    while N > 0:
        temp = temp * (N % 10)
        N = int(N / 10)
        
    N = temp
    cnt = cnt + 1

print(cnt)