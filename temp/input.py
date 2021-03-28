import sys
from collections import deque

queue = deque()

T = int(input())
N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]