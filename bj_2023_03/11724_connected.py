from collections import deque

N, M = map(int,input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int,input().split())
    adj[v1][v2] = 1
    adj[v2][v1] = 1

visited = [0]*(N+1)
Q =deque([])

ans = 0
while sum(visited[1:]) < N:
    if not Q:
        for i in range(1,N+1):
            if visited[i] == 0:
                Q.append(i)
                visited[i] = 1
                break
        else: break # while
    while Q:
        t = Q.popleft()
        if sum(adj[t]) == 0:
            visited[t] = 1
            break   # while Q
        elif sum(adj[t]) == 1 and adj[t][t] == 1:
            visited[t] = 1
            break

        for i in range(1,N+1):
            if adj[t][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = 1

        if not Q:
            ans += 1

print(ans)