def func(i, N, p):
    global ans

    if i == N:
        if ans < p:
            ans = p

    if p <= ans: return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                func(i+1,N,p*arr[i][j]/100)
                visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    visited = [0]*N
    p = 1

    func(0,N,p)

    print(f'#{tc} {ans*100:.6f}')