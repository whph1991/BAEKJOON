#2156
T = int(input())
N = []
dp = []

for i in range(0, T):
    N.append(int(input()))

if(T == 1):
    dp.append(N[0])
elif(T == 2):
    dp.append(N[0])
    dp.append(N[0] + N[1])
else:
    dp.append(N[0])
    dp.append(N[0] + N[1])
    dp.append(max(N[0] + N[1], N[0] + N[2], N[1] + N[2]))
    
    for i in range(3, T):
        dp.append(max(dp[i-2] + N[i], dp[i-3] + N[i-1] + N[i], dp[i-1]))

print(dp[T-1])