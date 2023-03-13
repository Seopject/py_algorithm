from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

N, M, T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
Q = deque([(0,0)])

bysword = 0
ans = 0

while Q:
    i, j = Q.popleft()
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            Q.append((ni,nj))
            visited[ni][nj] = visited[i][j] + 1
        elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 2 and visited[ni][nj] == 0:
            Q.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1
            bysword = abs(N-1-ni) + abs(M-1-nj) + visited[ni][nj]

if visited[N-1][M-1] == 0:
    visited[N-1][M-1] = 987654321


ans = min(bysword-1,visited[N-1][M-1]-1)
if ans <= T:
    if ans < 0:
        print('Fail')
    else:
        print(ans)
else:
    print('Fail')