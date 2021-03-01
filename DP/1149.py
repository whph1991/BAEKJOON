#1149
n = int(input())
cost = [[0]*3]*n

R, G, B =  map(int, input().split())
cost[0] = [R, G, B]

for i in range(1,n):
    R, G, B =  map(int, input().split())
    cost[i] = [R + min(cost[i-1][1], cost[i-1][2]), G + min(cost[i-1][0], cost[i-1][2]), B + min(cost[i-1][0], cost[i-1][1])]

print((min(cost[n - 1][0], cost[n - 1][1], cost[n - 1][2])))