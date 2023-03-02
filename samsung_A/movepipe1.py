import sys
input = sys.stdin.readline

def pipe(r,c,status):
    global ans
    if r == N-1 and c == N-1:
        ans += 1
        return
    elif r<0 or r>=N or c<0 or c>=N:
        return
    else:
        # 가로 상태
        if status == 0:
            if c+1 < N and arr[r][c+1] == 0:
                pipe(r,c+1,0)
            if r+1<N and c+1 < N and arr[r][c+1] == 0 and arr[r+1][c+1] == 0 and arr[r+1][c] == 0:
                pipe(r+1,c+1,1)

        # 대각선
        elif status == 1:
            if c+1 < N and arr[r][c+1] == 0:
                pipe(r,c+1,0)
            if r + 1 < N and c + 1 < N and arr[r][c + 1] == 0 and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0:
                pipe(r+1,c+1,1)
            if r+1 < N and arr[r+1][c] == 0:
                pipe(r+1,c,2)
        # 세로
        elif status == 2:
            if r + 1 < N and arr[r + 1][c] == 0:
                pipe(r + 1, c, 2)
            if r + 1 < N and c + 1 < N and arr[r][c + 1] == 0 and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0:
                pipe(r + 1, c + 1, 1)


N = int(input())
arr = [list(map(int,input().rstrip().split())) for _ in range(N)]
ans = 0
pipe(0,1,0)
print(ans)