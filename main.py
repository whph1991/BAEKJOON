#19238
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#입력
N, M, fule = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
customer = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
distance = [[0]*2 for _ in range(M)]
visited = [[0]*N for _ in range(N)]

def bfs():
  q = deque([[taxi[0] - 1, taxi[1] - 1, 0]])
  visited[taxi[0]-1][taxi[1]-1] = 1

  while q:
    x, y, dist = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 < nx < N and 0 < ny < N and visited[nx][ny] == 0 and matrix[nx][ny] == 0:
        q.append([nx, ny, dist + 1])
        visited[nx][ny] = 1

        for i in range(M):
          if customer[i][0]-1 == nx and customer[i][1]-1 == ny:
            distance[i] = dist + 1

bfs()

print(distance)