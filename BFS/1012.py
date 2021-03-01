#1012
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(_x, _y):
  q = deque([[_x, _y]])
  visited[_x][_y] = 1
  count = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
        q.append([nx, ny])
        visited[nx][ny] = 1
        count += 1

  return count

#입력
T = int(input())

for i in range(T):
  N, M, K = map(int, input().split())
  matrix = [[0]*M for _ in range(N)]
  visited = [[0]*M for _ in range(N)]
  ans = []

  for i in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 1

  for i in range(N):
    for j in range(M):
      if visited[i][j] == 0 and matrix[i][j] == 1:
        ans.append(bfs(i,j))

  print(len(ans))
  
