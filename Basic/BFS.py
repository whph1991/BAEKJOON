from collections import deque

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
N = 0

def do_something():
    return

def bfs(y, x):
    q = deque()

    q.append((y, x))
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 < ny <= N and 0 < nx <= N and not visited[ny][nx]:
                do_something()
                q.append((ny, nx))
                visited[ny][nx] = True