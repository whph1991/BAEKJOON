#9095
T = int(input())
N = []

for i in range(T):
    N.append(int(input()))

dp = [1, 2, 4]

for i in range(4, 11):
    dp.append(sum(dp[-3:]))
    
for i in range(T):
    print(dp[N[i] - 1])
