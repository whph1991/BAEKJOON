#9461
T = int(input())

for i in range(0, T):
    dp = []
    
    N = (int(input()))

    dp.append(1)
    dp.append(1)
    dp.append(1)
    dp.append(2)
    dp.append(2)

    for i in range(5, N):
        dp.append(dp[i-1] + dp[i-5])

    print(dp[N-1])