import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(R):
    global cnt
    visited[R] = cnt
    for idx in adjL[R]:
        if visited[idx] == -1:
            cnt += 1
            dfs(idx)

N, M, R = map(int,input().rstrip().split())
adjL = [[] for _ in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().rstrip().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)
for lst in adjL:
    lst.sort()

visited = [-1]*(N+1)
cnt = 0

dfs(R)

for i in range(1,N+1):
    print(visited[i])