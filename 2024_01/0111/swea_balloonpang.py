T = int(input())
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [0]*N
    maxVal = 0

    # 배열 저장
    for i in range(N):
        arr[i] = list(map(int,input().split()))

    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            for t in range(1,temp+1):
                for k in range(4):
                    if 0 <= i+di[k]*t < N and 0 <= j+dj[k]*t < M:
                        temp += arr[i+di[k]*t][j+dj[k]*t]
            if maxVal < temp:
                maxVal = temp
    print(f'#{tc} {maxVal}')

