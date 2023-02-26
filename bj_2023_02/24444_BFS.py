from collections import deque

N, M, R = map(int,input().split())
adjL = [[] for _ in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

visited = [0]*(N+1)
Q = deque([R])
visited[R] = 1

cnt = 2
while Q:
    t = Q.popleft()
    for i in sorted(adjL[t]):
        if visited[i] == 0:
            Q.append(i)
            visited[i] = cnt
            cnt += 1
for i in range(1,N+1):
    print(visited[i])