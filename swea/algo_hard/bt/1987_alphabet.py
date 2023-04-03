import sys
input = sys.stdin.readline

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

def go(stack,used):
    global ans

    if not stack:
        return

    i,j = stack[-1]
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and used[ord(arr[ni][nj])-65] == 0:
            stack.append((ni, nj))
            used[ord(arr[ni][nj])-65] = 1
            go(stack,used)
            stack.pop()
            used[ord(arr[ni][nj])-65] = 0

    else:
        ans = max(ans,len(stack))

N, M = map(int,input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]
ans = 0
stack = [(0,0)]
used = [0]*26
used[ord(arr[0][0])-65] = 1

go(stack,used)

print(ans)