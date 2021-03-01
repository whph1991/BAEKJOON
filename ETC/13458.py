#13458
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N

for A_i in A:
    A_i -= B
    
    if A_i < 0:
        continue
        
    if A_i % C == 0:
        ans += A_i // C
    else:
        ans += A_i // C + 1

print(ans)