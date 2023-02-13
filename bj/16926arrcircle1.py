import copy
N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = [[0]*M for _ in range(N)]

def turnarr(arr,ans,a,b,N,M):
        if a == N//2:
            for i in range(N):
                for j in range(M):
                    arr[i][j] = ans[i][j]
            return arr
        else:
            # 맨 위 행
            for i in range(b,M-1):
                ans[a][i] = arr[a][i+1]
            # 맨 아래 행
            for i in range(b+1,M-b):
                ans[-1*(a+1)][i] = arr[-1*(a+1)][i-1]
            # 맨 왼쪽 열
            for i in range(a+1,N-a):
                ans[i][b] = arr[i-1][b]

            for i in range(a,N-1-a):
                ans[i][-b-1] = arr[i+1][-b-1]

            a += 1
            b += 1
            return turnarr(arr,ans,a,b,N,M)

for i in range(R):
    turnarr(arr,ans,0,0,N,M)
for i in range(N):
    print(*arr[i])