from collections import deque
from copy import deepcopy

def bfs(list):
    global ans
    Q = deque(virus)
    while Q:
        i,j = Q.popleft()
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and list[ni][nj] == 0:
                Q.appendleft((ni,nj))
                list[ni][nj] = 2

    temp = 0
    for i in range(N):
        for j in range(M):
            if list[i][j] == 0:
                temp += 1
    ans = max(temp,ans)



def combi(s,k,idx):
    if s == k:
        temparr = [item[:] for item in arr]
        for v1, v2 in p:
            temparr[v1][v2] = 1
        bfs(temparr)

    else:
        for j in range(idx+1,len(blank)):
            p[s] = blank[j]
            combi(s+1,k,j)



N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

blank = []
virus = []
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))

p = [0]*3
combi(0,3,-1)
print(ans)
