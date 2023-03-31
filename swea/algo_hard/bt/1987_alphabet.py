# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

def go(stack,used,visited):
    global ans

    if not stack:
        return

    i,j = stack[-1]
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] not in used:
            stack.append((ni, nj))
            used.append(arr[ni][nj])
            visited[ni][nj] = visited[i][j] + 1
            go(stack,used,visited)
            stack.pop()
            used.pop()
            visited[ni][nj] = 0

    else:
        ans = max(ans,len(stack))

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
stack = [(0,0)]
used = [arr[0][0]]
visited[0][0] = 1

go(stack,used,visited)

print(ans)