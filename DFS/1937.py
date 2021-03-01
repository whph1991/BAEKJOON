#1937
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(_x, _y):
  if dp[_x][_y] == 0: 
    dp[_x][_y] = 1

    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and matrix[_x][_y] < matrix[nx][ny]:
          dp[_x][_y] = max(dp[_x][_y], dfs(nx, ny) + 1)

  return dp[_x][_y]
            
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
ans = 0

for i in range(N):
  for j in range(N):
    ans = max(ans, dfs(i, j))

print(ans)