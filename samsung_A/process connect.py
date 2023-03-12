# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 밖으로 이어지는지 검사
def connect(i,j,k):     # 행, 열, 방향
    ni, nj = i + di[k], j + dj[k]
    if 0>ni or N<=ni or 0>nj or N<=nj:  # 나가면 True 반환
        return True
    elif arr[ni][nj] == 1:  # 벽에 걸리면 경로 끝
        return False
    else:
        i,j = ni,nj
        return connect(i,j,k)   # 더 갈 수 있다면 진행

T = int(input())
for tc in range(1,T+1):
    N = int(input())    # N*N 배열
    arr = [list(map(int,input().split())) for _ in range(N)]
    core = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            # 코어라면
            if arr[i][j] == 1:
                # 00밖으로 못나가는 코어 필터링 후 저장
                for k in range(4):
                    if connect(i,j,k) != False and (i,j) not in core:
                        core.append((i,j))

    print(core)

    # 답 구하기
    ans = 0

