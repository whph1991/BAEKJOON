#14500
'''
1. 4칸 이동하는 모든 케이스
2. dfs로 이동 할 경우 'ㅗ' 모양은 별도 처리


'''

import sys

def dfs(x, y, value, cnt, visited):
  global ans

  visited[x][y] = True

  if cnt == 4:
    ans = max(ans, value)
    return 

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
      sum_value = value + matrix[nx][ny]
      visited[nx][ny] = True
      dfs(nx, ny, sum_value, cnt + 1, visited)
      visited[nx][ny] = False

def cross(x, y):
  cnt = 0
  arr = []
  value = matrix[x][y]

  for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        value += matrix[nx][ny]
        arr.append(matrix[nx][ny])
        cnt += 1

  if cnt == 4:
    value -= min(arr)

  return value


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
ans = 0
    
for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(i, j, matrix[i][j], 1, visited)
    ans= max(ans, cross(i, j))
    visited[i][j] = False

print(ans)