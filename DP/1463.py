#1463
X = int(input())
dp = [0 for _ in range(X+1)]

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1

    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        
print(dp[X])