from collections import deque

def bfs(list):
    global ans

    if not Q:
        print(list)
        temp = 0
        for i in range(N):
            for j in range(M):
                if list[i][j] == 0:
                    temp += 1
        ans = max(temp,ans)

    else:
        i, j = Q.popleft()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and list[ni][nj] == 0:
                Q.appendleft((ni,nj))
                list[ni][nj] = 2
                bfs(list)
def comb(i,k,idx):
    if i == k:
        for r,c in p:
            arr[r][c] = 1
        bfs(arr)
        for r,c in p:
            arr[r][c] = 0
    else:
        for j in range(idx+1,len(blank)):
            p[i] = blank[j]
            comb(i+1,k,idx)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
virus = []
blank = []
p = [0]*3
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            blank.append((i,j))

Q = deque(virus)
comb(0,3,-1)
print(ans)