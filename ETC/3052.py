#3052
ans = 0
N = [int(input()) for _ in range(10)]
visited = [0 for _ in range(42)]

for i in range(10):
  visited[N[i] % 42] = 1

for i in range(42):
  ans += visited[i]

print(ans)