def func(i,N):
    global answer

    if i == N:
        if answer > sum(col):
            answer = sum(col)
    elif sum(col) > answer: return
    else:
        for j in range(N):
            if col[j] == 0:
                col[j] = arr[i][j]
                func(i+1,N)
                col[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    col = [0]*N
    answer = 99999999

    func(0,N)
    print(f'#{tc} {answer}')

