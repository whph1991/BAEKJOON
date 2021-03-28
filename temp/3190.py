#3190
import sys


# 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#입력
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
cmd = {}

for i in range(L):
  ctime, c = input().split()
  cmd[int(ctime)] = c

matrix = [[0]*N for _ in range(N)]

for i in range(len(apple)):
  x, y = apple[i]
  matrix[x-1][y-1] = 1

direction = 0
ctime = 0
matrix[0][0] = -1


while 1:
  ctime += 1

  nx = x + dx[direction]
  ny = y + dy[direction]

  if nx < 0 or nx > N or ny < 0 or ny > N or matrix[nx][ny] == -1:
    break

  if matrix[nx][ny] == 1:
    matrix[nx][ny] = -1

  if matrix[nx][ny] == 0:
    matrix[nx][ny] = -1
    


  

  

