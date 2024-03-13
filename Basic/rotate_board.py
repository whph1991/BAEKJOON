N = 5
board = [[i*N + j for j in range(N)] for i in range(N)]

def rotate_board(board):
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[N-j-1][i]
    return new_board

[print(row) for row in board]
print()
[print(row) for row in rotate_board(board)]