from collections import deque


def do_something(perm):
    print(perm)


M = 3
some_list = [1, 2, 3, 4]

visited = [False] * len(some_list) # 중복 포함 여부
result = []


def dfs(perm: deque):
    if len(perm) == M:
        do_something(perm)
        result.append(perm)
        return

    for i, val in enumerate(some_list):
        if visited[i]:
            continue

        # i-th 포함
        perm.append(val)
        # visited[i] = True
        dfs(perm)

        # i-th 삭제
        perm.pop()
        # visited[i] = False


dfs(deque())
print(len(result))