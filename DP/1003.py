#1003
T = int(input())
N = []

for i in range(T):
    N.append(int(input()))

dp = [[1,0],[0,1]]

for i in range(40):
    dp.append([dp[i][0] + dp[i+1][0], dp[i][1] + dp[i+1][1]])
    
for i in range(T):
    print("%d %d" % (dp[N[i]][0], dp[N[i]][1]))