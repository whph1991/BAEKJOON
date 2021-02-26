#2667
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#입력
N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = []

def bfs(_x, _y):
  q = deque([[_x, _y]])
  visited[_x][_y] = 1
  count = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and matrix[nx][ny] == '1':
        q.append([nx, ny])
        visited[nx][ny] = 1
        count += 1

  return count

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0 and matrix[i][j] == '1':
      ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for i in ans:
  print(i)