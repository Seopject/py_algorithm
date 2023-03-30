def promising(i,j):
    for di, dj in [[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, j+dj
        while 0<=ni<N and 0<=nj<N:
            if board[ni][nj]:   # 칸이 채워져있다면
                return 0
            ni, nj = ni+di, nj+dj
    return 1    # i,j에 퀸 가능

# col에 놓아진 적이 있으면 표시하는 배열 써보기
# 대각선 배열 각 행 열 1~N하면 각 칸의 합이 N
# 이미 대각선에 놓여진적이 있었는가 왼대각선 오른대각선 d1,d2설정해서 해보기

def f(i, N):
    global cnt
    if i == N:  # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i,j):
                board[i][j] = 1
                f(i+1,N)
                board[i][j] = 0


N = int(input())

board = [[0]*N for _ in range(N)]
cnt = 0
f(0,N)
print(cnt)