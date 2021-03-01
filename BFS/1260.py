#1260
N,M,V=map(int,input().split())

matrix=[[0]*(N+1) for i in range(N+1)]

# Matrix 생성
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
    
# 체크 리스트
dfs_visit_list=[0]*(N+1)
bfs_visit_list=[0]*(N+1)

def dfs(V):
    dfs_visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(dfs_visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    bfs_visit_list[V]=1 #방문한 점 1으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(bfs_visit_list[i]==0 and matrix[V][i]==1):
                queue.append(i)
                bfs_visit_list[i]=1

dfs(V)
print()
bfs(V)