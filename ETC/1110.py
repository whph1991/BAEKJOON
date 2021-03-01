#1110
firstNumber = int(input())

cnt = 0
n = firstNumber
while True:
    cnt += 1
    n = (n%10)*10+(int(n/10)+n%10)%10
    
    if firstNumber == n:
        break

print(cnt)