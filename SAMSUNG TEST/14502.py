#14502
from collections import deque
from copy import deepcopy


# N, M = 4, 6
# MAP = [[0, 0, 0, 0, 0, 0],
#        [1, 0, 0, 0, 0, 2],
#        [1, 1, 1, 0, 0, 2],
#        [0, 0, 0, 0, 0, 2]]

N, M = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(N)]

# 동 서 남 북
dx = [+1, -1, 0, 0]
dy = [0, 0, -1, +1]

answer = 0

# 바이러스 위치 및 빈 공간 확인

virus = []
candidates = []

for row in range(N):
    for col in range(M):
        if MAP[row][col] == 2:
            virus.append([row, col])
        elif MAP[row][col] == 0:
            candidates.append([row, col])

# 임의의 빈 공간 위치에 3개의 벽을 세우는 방법
L = len(candidates)
for i in range(L):
    for j in range(i+1, L):
        for k in range(j+1, L):
            MAP_1 = deepcopy(MAP)
            row, col = candidates[i]
            MAP_1[row][col] = 1
            row, col = candidates[j]
            MAP_1[row][col] = 1
            row, col = candidates[k]
            MAP_1[row][col] = 1

            # 바이러스 확산
            q = deque(virus)
            while q:
                row, col = q.popleft()

                for dir in range(4):
                    next_row = row + dx[dir]
                    next_col = col + dy[dir]

                    if 0 <= next_row < N and 0 <= next_col < M:
                        if MAP_1[next_row][next_col] == 0:
                            MAP_1[next_row][next_col] = 2
                            q.append([next_row, next_col])

            # 안전 공간 카운트
            cnt = 0
            for row in range(N):
                for col in range(M):
                    if MAP_1[row][col] == 0:
                        cnt += 1

            answer = max(answer, cnt)
print(answer)

# debug
# for row in range(N):
#     print([MAP_1[row][col] for col in range(M)])