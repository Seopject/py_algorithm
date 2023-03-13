from collections import deque

# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input())    # 보드 크기
arr = [[0]*N for _ in range(N)]

K = int(input())    # 사과 개수
for i in range(K):
    r, c = map(int,input().split())
    arr[r-1][c-1] = 1

L = int(input())    # 뱀 방향전환
dir = {}
for i in range(L):
    sec, direction = map(str,input().split())
    dir[int(sec)] = direction

second = 0
k = 0
Q = deque([(0,0)])
snake = deque([(0,0)])
arr[0][0] = 2
while Q:
    i,j  = Q.popleft()
    ni, nj = i+di[k], j+dj[k]
    second += 1
    if 0<=ni<N and 0<=nj<N:     # 배열 범위 내
        if arr[ni][nj] == 1:    # 사과라면
            snake.append((ni,nj))
            Q.append((ni,nj))
            arr[ni][nj] = 2

        elif arr[ni][nj] == 2:  # 뱀의 몸이라면
            print(second)
            break # while
        elif arr[ni][nj] == 0:  # 아무것도 아니면
            Q.append((ni,nj))
            arr[ni][nj] = 2
            snake.append((ni,nj))
            arr[snake[0][0]][snake[0][1]] = 0
            snake.popleft()
    else:
        print(second)
        break

    if second in dir:
        if dir.get(second) == 'L':
            k = (k+3)%4
        elif dir.get(second) == 'D':
            k = (k+1)%4

