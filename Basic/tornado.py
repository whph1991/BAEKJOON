N = 5
board = [[0]*N for _ in range(N)]

# 서, 남, 동, 북
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)


def tornado():
    x = y = int(N/2)
    move_cnt = direction = number = 0
    distance = 1

    while True:
        move_cnt += 1
        for _ in range(distance):
            ny = y + dy[direction]
            nx = x + dx[direction]

            if (ny, nx) == (0, -1):
                return

            number += 1
            board[ny][nx] = number

            y = ny
            x = nx

        if move_cnt == 2:
            move_cnt = 0
            distance += 1

        direction = (direction + 1) % 4


tornado()
[print(row) for row in board]
