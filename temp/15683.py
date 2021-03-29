#15683
import sys
import copy
from collections import deque

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 사각지대 카운트
def check_black():
  cnt = 0

  for i in range(N):
    for j in range(M):
      if matrix[i][j] == 0:
        cnt += 1

  return cnt

# 감시 영역 확인
def solve(_camera_idx):
  
  # 종료 조건
  if _camera_idx == len(camera):
    ans = min(ans, check_black())
    return

  x, y, camera_type = camera[_camera_idx]

  for i in range(4):
    
    if camera_type == 1:
      nx = x
      ny = y

      while 1:
        nx += dx[i]
        ny += dy[i]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 6:
          matrix[nx][ny] = '#'

    if camera_type == 2:
      nx = x
      ny = y

      while 1:
        nx += dx[i]
        ny += dy[i]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 6:
          matrix[nx][ny] = '#'

      nx = x
      ny = y

      while 1:
        nx += dx[(i+2)%4]
        ny += dy[(i+2)%4]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 6:
          matrix[nx][ny] = '#'

    solve(_camera_idx)


# 카메라 정보 추출
def check_camera():
  for i in range(N):
    for j in range(M):
      if 1 <= matrix[i][j] <= 5:
        camera.append(i, j, matrix[i][j])


# 입력
N, M = map(int, input().split())
org_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix = copy.deepcopy(org_matrix)
camera = []
ans = 999

check_camera()

for i in range(4):
  x, y, camera_type = camera[0]

  solve(0)

print(ans)
