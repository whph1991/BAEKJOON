#2178
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#입력
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(_x, _y, _count):
  q = deque([[_x, _y, _count]])

  while q:
    x, y, count = q.popleft()

    if x == N-1 and y == M-1:
      return count

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and matrix[nx][ny] == '1':
        q.append([nx, ny, count + 1])
        visited[nx][ny] = 1

print(bfs(0, 0, 1))