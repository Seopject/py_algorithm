N = int(input()) # 노드 수
adj = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

p = [0]*(N+1)
visited = [0]*(N+1)
stack = [1]
visited[1] = 1

while stack:
    for temp in adj[stack[-1]]:
        if visited[temp] == 0:
            p[temp] = stack[-1]
            stack.append(temp)
            visited[temp] = 1
            break

    else:
        stack.pop()

for i in range(2,N+1):
    print(p[i])

