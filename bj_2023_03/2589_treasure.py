from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
search = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            search.append((i,j))

ans = 0
while search:
    Q = deque([search.popleft()])
    visited = [[0]*M for _ in range(N)]
    r, c = Q[0]
    visited[r][c] = 1
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 'L' and visited[ni][nj] == 0:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
                if ans < visited[ni][nj]:
                    ans = visited[ni][nj]

print(ans-1)
