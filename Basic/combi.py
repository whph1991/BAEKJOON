from collections import deque

M = 3
some_list = [1, 2, 3, 4]

def do_something(combi):
    print(combi)

def dfs(combi: deque, depth: int):
    if len(combi) == M:
        do_something(combi)
        return
    elif depth == len(some_list):
        return

    # 현재 depth 값 포함
    combi.append(some_list[depth])
    dfs(combi, depth+1)

    # 현재 depth 값 미포함
    combi.pop()
    dfs(combi, depth + 1)

dfs(deque(), 0)
