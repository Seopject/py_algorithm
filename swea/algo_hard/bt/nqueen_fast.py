def promising(i,j):
    if col[j] or d1[i+j] or d2[i + N - 1 - j]:
        return 0
    return 1

# col에 놓아진 적이 있으면 표시하는 배열 써보기
# 대각선 배열 각 행 열 1~N하면 각 칸의 합이 N
# 이미 대각선에 놓여진적이 있었는가 왼대각선 오른대각선 d1,d2설정해서 해보기

def f(i, N):
    global cnt
    if i == N:  # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and d1[i+j]==0 and d2[i+N-1-j]==0:
                col[j] = 1
                d1[i+j] = 1
                d2[i+N-1-j] = 1
                f(i+1,N)
                col[j] = 0
                d1[i + j] = 0
                d2[i + N - 1 - j] = 0


N = int(input())

col = [0]*N
d1 = [0]*(N+N-1)    # / diag
d2 = [0]*(N+N-1)    # \ diag

cnt = 0
f(0,N)
print(cnt)