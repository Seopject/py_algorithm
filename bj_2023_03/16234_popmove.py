from collections import deque
import copy

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

N, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

cnt = [0]*2000

for ppp in range(2001):
    temp_arr = copy.deepcopy(arr)
    visited = [[0]*N for _ in range(N)]
    cnt_temp = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: pass
            else:
                visited[i][j] = 1
                Q = deque([(i,j)])
                temp_pop = arr[i][j]
                save_Q = deque([(i,j)])

                while Q:
                    ti, tj = Q[0]
                    for k in range(4):
                        ni, nj = ti+di[k],tj+dj[k]
                        if 0<=ni<N and 0<=nj<N and L <= abs(arr[ni][nj] - arr[ti][tj]) <=R and visited[ni][nj] ==0:
                            visited[ni][nj] = 1
                            temp_pop += arr[ni][nj]
                            save_Q.append((ni,nj))
                            Q.append((ni,nj))
                    else:
                        Q.popleft()

                if len(save_Q) == 1: pass
                else:
                    temp_pop = temp_pop//len(save_Q)
                    for r,c in save_Q:
                        temp_arr[r][c] = temp_pop
                    cnt_temp = True

    if cnt_temp == True:
        cnt[ppp] = 1
        cnt_temp = False

    if cnt[ppp] == 0:
        print(ppp)
        break

    arr = copy.deepcopy(temp_arr)