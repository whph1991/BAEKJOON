#13460
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    #init
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if Board[i][j] == 'R':
                rx, ry = i, j
            elif Board[i][j] == 'B':
                bx, by = i, j

    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if Board[nbx][nby] != 'O':      # 실패 조건이 아니면
                if Board[nrx][nry] == 'O':  # 성공 조건
                    return depth

                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:            # 이동거리가 많은 것을
                        nrx -= dx[i]           # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if visited[nrx][nry][nbx][nby] is False:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth+1))
    return -1

def move(x, y, dx, dy):
    cnt = 0

    while Board[x+dx][y+dy] != '#' and Board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

# 입력
N, M = map(int, input().split())
Board = [list(input().rstrip()) for _ in range(N)]

q = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

print(bfs())