# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

def func(i,j,stack):
    global ans

    if len(stack) == 7:
        temp = ''.join(stack)
        if temp not in visited:
            visited[temp] = True
            ans += 1
            return

    else:
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<4 and 0<=nj<4:
                tmp = [i for i in stack] + [arr[ni][nj]]
                if ''.join(tmp) not in visited:
                    func(ni,nj,tmp)

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(str,input().split())) for _ in range(4)]
    ans = 0
    visited = {}

    for i in range(4):
        for j in range(4):
            func(i,j,[arr[i][j]])

    print(f'#{tc} {ans}')