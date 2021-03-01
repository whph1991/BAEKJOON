#1912
T = int(input())
N = []
dp = []

N = list(map(int, input().split()))

dp.append(N[0])

for i in range(1, T):
    dp.append(max(dp[i-1] + N[i], N[i]))

print(max(dp))