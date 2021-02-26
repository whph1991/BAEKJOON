#2606
from collections import deque

#입력
N = int(input())
M = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
  x, y = map(int, input().split())
  matrix[x][y] = matrix[y][x] = 1

visited = [0]*(N+1)

def bfs(_v):
  q = deque([_v])
  visited[_v] = 1
  count = 0

  while q:
    v = q.popleft()

    for i in range(1, N+1):
      if visited[i] == 0 and matrix[v][i] == 1:
        q.append(i)
        visited[i] = 1
        count += 1

  return count

print(bfs(1))  