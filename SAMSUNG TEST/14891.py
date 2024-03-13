#14891

board = [list(map(int, input())) for _ in range(4)]
K = int(input())
querys = [list(map(int, input().split())) for _ in range(K)]

# rotate
def rotate(line, dir):
    if dir == 1:
        line.insert(0, line[-1])
        del line[-1]
    elif dir == -1:
        line.append(line[0])
        del line[0]

# case
for query in querys:
    row = query[0] - 1
    dir = query[1]

    dirs = [0]*4
    dirs[row] = dir

    left = row - 1
    while True:
        right = left + 1
        if right >= 4 or left < 0:
            break

        if board[left][2] == board[right][6]:
            break
        else:
            dirs[left] = dirs[right] * (-1)
            left -= 1

    right = row + 1
    while True:
        left = right - 1
        if right >= 4 or left < 0:
            break

        if board[left][2] == board[right][6]:
            break
        else:
            dirs[right] = dirs[left] * (-1)
            right += 1

    for row in range(4):
        rotate(board[row], dirs[row])

score = 0
for row in range(4):
    if board[row][0]:
        score += 2**row

print(score)


