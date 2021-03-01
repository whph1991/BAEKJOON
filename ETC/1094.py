#1094
X = int(input())
n = 64
ans = 0

while X > 0:
    if X-n >= 0:
        X = X-n
        ans = ans + 1
    n = n/2
print(ans)