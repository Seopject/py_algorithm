from collections import deque
def bfs(list,visited):
    global ans

    while Q:
        i,j = Q.popleft()

        if visited[i][j] >= ans: return

        if i == (N-1) and j == (M-1):
            ans = min(ans,visited[i][j])
            return
        else:
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M and list[i][j] == 0 and visited[ni][nj] == 0:
                    Q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1



N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
wall = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    wall.append((i,j))


Q = deque([(0,0)])
ans = 99999999

for i in range(len(wall)):
    wi, wj = wall[i]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    temp_arr = [item[:] for item in arr]
    temp_arr[wi][wj] = 0
    bfs(temp_arr,visited)

if ans == 99999999:
    print(-1)
else:
    print(ans)
