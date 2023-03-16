from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for rain in range(101):
    visited = [[0]*N for _ in range(N)]
    tempans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                visited[i][j] = 1
            elif visited[i][j] == 1: pass
            else:
                visited[i][j] = 1
                Q = deque([(i,j)])
                while Q:
                    r,c = Q.popleft()
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0<=nr<N and 0<=nc<N and arr[nr][nc] > rain and visited[nr][nc] == 0:
                            Q.append((nr,nc))
                            visited[nr][nc] = 1
                else:
                    tempans += 1

    if ans < tempans:
        ans = tempans

print(ans)