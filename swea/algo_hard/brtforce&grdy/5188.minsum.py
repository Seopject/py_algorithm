def minsum(i,j,s):
    global answer

    if (i,j) == (N-1,N-1):
        if s < answer:
            answer = s

    elif s > answer:
        return

    else:
        # 우
        if 0<=j+1<N:
            s += arr[i][j+1]
            minsum(i,j+1,s)
            s -= arr[i][j+1]
        if 0<=i+1<N:
            s += arr[i+1][j]
            minsum(i+1,j,s)
            s -= arr[i+1][j]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    i, j = 0, 0
    answer = 9999999
    minsum(i,j,arr[i][j])
    print(f'#{tc} {answer}')