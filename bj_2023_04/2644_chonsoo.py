from collections import deque

N = int(input())
A, B = map(int,input().split())
m = int(input())
adj = [[] for _ in range(N+1)]
for i in range(m):
    v1, v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visited = [-1]*(N+1)

Q = deque([])
for temp in adj[A]:
    Q.append(temp)
    visited[temp] = 1

while Q:
    t = Q.popleft()
    for temp in adj[t]:
        if visited[temp] == -1:
            Q.append(temp)
            visited[temp] = visited[t] + 1

print(visited[B])