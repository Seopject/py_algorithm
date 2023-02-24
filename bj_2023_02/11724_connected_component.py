from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global cnt
    Q.append(visited.index(0))
    while Q:
        t = Q.popleft()
        visited[t] = 1
        for i in range(1,N+1):
            if arr[t][i] == 1 and visited[i] == 0:
                Q.append(i)
    cnt += 1

N, M = map(int,input().rstrip().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int,input().rstrip().split())
    arr[v1][v2] = 1
    arr[v2][v1] = 1

visited = [-1] + [0]*N
Q = deque([])
cnt = 0
while 0 in visited:
    bfs()
print(cnt)