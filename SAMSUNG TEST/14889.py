# 14889
import math

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [False]*N
min_value = math.inf

def dfs(idx, k):
    global min_value

    if k == N//2:
        ateam = []
        asum = 0
        for i in range(N):
            if visited[i]:
                ateam.append(i)

        for row in ateam:
            for col in ateam:
                asum += board[row][col]

        bteam = []
        bsum = 0
        for i in range(N):
            if not visited[i]:
                bteam.append(i)

        for row in bteam:
            for col in bteam:
                bsum += board[row][col]

        min_value = min(min_value, abs(asum - bsum))

    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(i, k + 1)
                visited[i] = False

dfs(0, 0)

print(min_value)



