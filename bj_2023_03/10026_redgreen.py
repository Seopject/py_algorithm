di = [0,1,0,-1]
dj = [1,0,-1,0]
N = int(input())
arr = [list(input()) for _ in range(N)]

# 적록색약 X
visitedNone = [[0]*N for _ in range(N)]
ans = [0,0]
for i in range(N):
    for j in range(N):
        if visitedNone[i][j] == 0:
            stack = []
            stack.append((i,j))
            status = arr[i][j]
            visitedNone[i][j] = 1
            while stack:
                r,c = stack[-1]
                for k in range(4):
                    nr, nc = r+di[k], c+dj[k]
                    if 0<=nr<N and 0<=nc<N and arr[nr][nc] == status and visitedNone[nr][nc] == 0:
                        stack.append((nr,nc))
                        visitedNone[nr][nc] = 1
                        break
                else:
                    stack.pop()

                if not stack:
                    ans[0] += 1

# 적록색약 O
visitedRG = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visitedRG[i][j] == 0:
            stack = []
            stack.append((i,j))
            visitedRG[i][j] = 1
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                status = ['R','G']
            else:
                status = [arr[i][j]]
            while stack:
                r, c = stack[-1]
                for k in range(4):
                    nr, nc = r + di[k], c + dj[k]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in status and visitedRG[nr][nc] == 0:
                        stack.append((nr, nc))
                        visitedRG[nr][nc] = 1
                        break
                else:
                    stack.pop()

                if not stack:
                    ans[1] += 1

print(*ans)