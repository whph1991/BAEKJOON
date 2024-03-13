#15683
import math
from copy import deepcopy

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

# dir 0:동 1:서 2:남 3:북

# 카메라 리스트 생성
cameras = [] # type, row, col, dir
min_value = 0
for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            min_value += 1
        if board[row][col] != 0 and board[row][col] != 6:
            cameras.append([board[row][col], row, col, 0])

def update_lay_view(board, row, col, dir):
    dcol = [1, -1, 0, 0]
    drow = [0, 0, -1, 1]

    nrow = row
    ncol = col
    while True:
        nrow += drow[dir]
        ncol += dcol[dir]

        if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M or board[nrow][ncol] == 6:
            return
        board[nrow][ncol] = '#'

def check_range(board, cameras):
    for camera in cameras:
        if camera[0] == 1:
            update_lay_view(board, camera[1], camera[2], camera[3])
        elif camera[0] == 2:
            if camera[3] == 0:
                update_lay_view(board, camera[1], camera[2], 0)
                update_lay_view(board, camera[1], camera[2], 1)
            else:
                update_lay_view(board, camera[1], camera[2], 2)
                update_lay_view(board, camera[1], camera[2], 3)
        elif camera[0] == 3:
            if camera[3] == 0:
                update_lay_view(board, camera[1], camera[2], 3)
                update_lay_view(board, camera[1], camera[2], 0)
            elif camera[3] == 1:
                update_lay_view(board, camera[1], camera[2], 0)
                update_lay_view(board, camera[1], camera[2], 2)
            elif camera[3] == 2:
                update_lay_view(board, camera[1], camera[2], 2)
                update_lay_view(board, camera[1], camera[2], 1)
            elif camera[3] == 3:
                update_lay_view(board, camera[1], camera[2], 1)
                update_lay_view(board, camera[1], camera[2], 3)
        elif camera[0] == 4:
            if camera[3] == 0:
                update_lay_view(board, camera[1], camera[2], 1)
                update_lay_view(board, camera[1], camera[2], 3)
                update_lay_view(board, camera[1], camera[2], 0)
            elif camera[3] == 1:
                update_lay_view(board, camera[1], camera[2], 3)
                update_lay_view(board, camera[1], camera[2], 0)
                update_lay_view(board, camera[1], camera[2], 2)
            elif camera[3] == 2:
                update_lay_view(board, camera[1], camera[2], 0)
                update_lay_view(board, camera[1], camera[2], 2)
                update_lay_view(board, camera[1], camera[2], 1)
            elif camera[3] == 3:
                update_lay_view(board, camera[1], camera[2], 2)
                update_lay_view(board, camera[1], camera[2], 1)
                update_lay_view(board, camera[1], camera[2], 3)
        elif camera[0] == 5:
            update_lay_view(board, camera[1], camera[2], 0)
            update_lay_view(board, camera[1], camera[2], 1)
            update_lay_view(board, camera[1], camera[2], 2)
            update_lay_view(board, camera[1], camera[2], 3)

    cnt = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                cnt += 1

    # for row in range(N):
    #     print([board[row][col] for col in range(M)])
    # print()

    return cnt

def dfs(key, cameras):
    global min_value
    if key == len(cameras):
        min_value = min(min_value, check_range(deepcopy(board), cameras))
        return

    for i in range(4):
        if cameras[key][0] == 5:
            dfs(key + 1, deepcopy(cameras))
            break
        elif cameras[key][0] == 2:
            if i == 2:
                break
            cameras[key][-1] = i
            dfs(key + 1, deepcopy(cameras))
        else:
            cameras[key][-1] = i
            dfs(key + 1, deepcopy(cameras))

dfs(0, deepcopy(cameras))
print(min_value)
