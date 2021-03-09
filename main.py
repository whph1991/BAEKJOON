#14502
'''
1. 벽을 세운다
2. 바이러스를 퍼트린다
3. 안전 영역을 구한다
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs():
  count = 0
  cur_matrix = copy.deepcopy(matrix)

  for row in range(N):
    for col in range(M):
      if count == 3:
        break;
      cur_matrix[row][col] = 1
      count += 1
