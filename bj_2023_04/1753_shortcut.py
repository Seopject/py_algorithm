def dijk(S,V):
    U = [0]*(V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adj[S][i]

    for _ in range(V):
        minV = INF
        temp = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                temp = i
                minV = D[i]
        U[temp] = 1
        for v in range(V+1):
            if 0 < adj[temp][v] < INF:
                D[v] = min(D[v], D[temp] + adj[temp][v])

V, E = map(int,input().split())
s = int(input())
INF = 9999999
adj = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adj[i][i] = 0
D = [0] * (V + 1)
for i in range(E):
    v1, v2, w = map(int,input().split())
    adj[v1][v2] = w

dijk(s,V)
for i in range(1,V+1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])