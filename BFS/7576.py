#7576
import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#입력
M, N = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = deque()

def bfs():
  count = 0

  for i  in range(N):
    for j in range(M):
      if matrix[i][j] == 1:
        q.append([i, j, 0])
        visited[i][j] = 1

  while q:
    x, y, count = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and matrix[nx][ny] == 0:
        q.append([nx, ny, count+1])
        visited[nx][ny] = 1
        matrix[nx][ny] = count+1

  for b in matrix:
    if 0 in b:
      count = -1

  return count

print(bfs())  