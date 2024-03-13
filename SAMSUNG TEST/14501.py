#14501


# N = 7
# T = [3, 5, 1, 1, 2, 4, 1]
# P = [10, 20, 10, 20, 15, 40, 200]

def dp(day, p):
    global answer
    if day == N:
        answer = max(answer, p)
        return

    if day + T[day] <= N:
        dp(day + T[day], p + P[day])

    dp(day + 1, p)

N = int(input())
T = []
P = []

for _ in range(N):
    Ti, Pi = map(int, input().split())
    T.append(Ti)
    P.append(Pi)

answer = 0
for i in range(N):
    dp(i, 0)

print(answer)

def dfs(today, p):
    if today >= N or today + T[today] > N:
        return p

    candidates = []
    for i in range(today, N):
        if i < N and i + T[i] <= N:
            candidates.append(dfs(i + T[i], p + P[i]))

        candidates.append(p)
    return max(candidates)

N = int(input())
T = []
P = []

for _ in range(N):
    Ti, Pi = list(map(int, input().split()))
    T.append(Ti)
    P.append(Pi)

print(dfs(0, 0))