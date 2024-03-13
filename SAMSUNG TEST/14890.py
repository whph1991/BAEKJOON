#14890

N, L = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
stairs = [False] * N

def dfs(idx, key, line):
    global cnt
    if idx == N-1:
        cnt += 1
        return

    if line[idx] == line[idx + 1]:
        dfs(idx+1, key+1, line)
    # 높아지는 경우
    elif line[idx+1] - line[idx] == 1:
        if key >= L:
            ret = True
            for i in range(L):
                if idx-i < 0 or stairs[idx-i]:
                    ret = False
                    break
            if ret:
                for i in range(L):
                    stairs[idx-i] = True
                dfs(idx+1, 1, line)
    # 낮아지는 경우
    elif line[idx] - line[idx + 1] == 1:
        if not stairs[idx +1]:
            ret = True
            for i in range(1, L):
                if idx+1+i >= N:
                    ret = False
                    break

                if stairs[idx+1+i]:
                    ret = False
                    break

                if line[idx+1] != line[idx+1+i]:
                    ret = False
            if ret:
                for i in range(L):
                    stairs[idx+1+i] = True
                dfs(idx+L, 1, line)

for col in range(N):
    board.append([board[row][col] for row in range(N)])

for row in range(2*N):
    stairs = [False] * N
    dfs(0, 1, board[row])

print(cnt)

