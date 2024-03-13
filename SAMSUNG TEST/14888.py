#14888
import math
from copy import deepcopy
from collections import deque

max_value = -math.inf
min_value = math.inf

def cal(ret, A, op):
    if op == 0:
        ret += A
    elif op == 1:
        ret -= A
    elif op == 2:
        ret *= A
    else:
        ret = int(ret / A)
    return ret

def dfs(ret, Alist, oplist):
    global min_value, max_value
    if Alist:
        A = Alist.popleft()
        for i in range(4):
            if oplist[i]:
                if i == 2 and A == 0:
                    continue
                oplist[i] -= 1
                dfs(cal(ret, A, i), deepcopy(Alist), deepcopy(oplist))
                oplist[i] += 1
    else:
        min_value = min(min_value, ret)
        max_value = max(max_value, ret)

N = int(input())
Alist = deque(list(map(int, input().split())))
oplist = list(map(int, input().split()))

ret = Alist.popleft()
dfs(ret, Alist, oplist)

print(max_value)
print(min_value)