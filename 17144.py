#17144

import sys
import copy

# 이동방향 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 확산
def diffusion():
  global matrix, nmatrix
  nmatrix = copy.deepcopy(matrix)

  for i in range(R):
    for j in range(C):
      if matrix[i][j] > 0:
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]

          if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != -1 and matrix[i][j] >= 5:
            nmatrix[nx][ny] += matrix[i][j] // 5
            nmatrix[i][j]   -= matrix[i][j] // 5

  matrix = nmatrix


# 이동
def move(_x, _y, _dir, idx):
  x = _x
  y = _y

  if idx == 0:  
    for i in range(4):
      while True:
        nx = x + dx[_dir[i]]
        ny = y + dy[_dir[i]]

        if nx == _x and ny == _y:
          matrix[_x][_y+1] = 0
          break

        if 0 <= nx <= _x and 0 <= ny < C:
          matrix[x][y] = matrix[nx][ny]
          x = nx
          y = ny
        else:
          break
  else:
    for i in range(4):
      while True:
        nx = x + dx[_dir[i]]
        ny = y + dy[_dir[i]]

        if nx == _x and ny == _y:
          matrix[_x][_y+1] = 0
          break

        if _x <= nx < R and 0 <= ny < C:
          matrix[x][y] = matrix[nx][ny]
          x = nx
          y = ny
        else:
          break

  matrix[_x][_y] = -1

# 남은 미세먼지 양
def sum_dust():
  # 공기 청정기 위치 -1 2칸
  ans = 2

  #print(matrix)
  for i in range(R):
      ans += sum(matrix[i])
  
  print(ans)


# 입력
R, C, T = map(int,input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
nmatrix = []
air_clean = 0

# 공기 청정기 위치 확인
for i in range(R):
  if matrix[i][0] == -1:
    air_clean = i
    break

for i in range(T):
  diffusion()
  move(air_clean,   0, [0, 1, 2, 3], 0)
  move(air_clean+1, 0, [2, 1, 0, 3], 1)
  
sum_dust()