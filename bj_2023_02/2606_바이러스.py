N = int(input()) # 컴터 수
pair = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(pair):
    r1, r2 = map(int,input().split())
    arr[r1][r2] = 1
    arr[r2][r1] = 1
stack = [1]
visited = [0,1] + [0]*(N-1)

while stack:
    for i in range(1,N+1):
        if arr[stack[-1]][i] == 1 and visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            break
    else:
        stack.pop()

print(sum(visited)-1)