#11724
import sys
from collections import deque

def bfs():
  result = 0
  q = deque()

  for i in range(1, N+1):
    if not visited[i]:
      visited[i] = True
      q.append(i)
      result += 1

      while q:
        node = q.popleft()

        for j in linkedlist[node]:
          if not visited[j]:
            visited[j] = True
            q.append(j)
          
  print(result)

N, M = map(int, sys.stdin.readline().split())

linkedlist = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  linkedlist[u].append(v)
  linkedlist[v].append(u)

bfs()