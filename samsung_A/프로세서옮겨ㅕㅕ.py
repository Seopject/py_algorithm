# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 해당 코어가 밖으로 나갈 수 있는지 판단
def isout(i,j,k): # 행, 열, 방향
    ni, nj = i+di[k], j+dj[k]
    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
        return False
    elif ni < 0 or ni>=N or nj<0 or nj>=N:
        return True
    else:
        return isout(ni,nj,k)

# 해당 코어 바깥까지의 거리
def howlong(i,j,k,cnt): # 행, 열, 방향
    global tempans
    ni, nj = i+di[k], j+dj[k]
    if 0<=ni<N and 0<=nj<N and temp[ni][nj] == 1:
        return False
    elif ni<0 or ni>=N or nj<0 or nj>=N:
        return cnt
    else:
        temp[ni][nj] = 1
        cnt += 1
        return howlong(ni,nj,k,cnt)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    core = [[] for _ in range(12)]
    corenum = 0     # 코어 번호 설정
    # 코어 찾고 나갈 수 있는지 판단
    for i in range(1,N-1):
        for j in range(1,N-1):
            # 배열에 코어가 있다면
            if arr[i][j] == 1:
                for k in range(4):
                    if isout(i,j,k) == True:
                        core[corenum].append((i,j,k))
            # 받았으면 idx += 1
            if core[corenum]:
                corenum += 1
    print(core)
    ans = 999999
    # 가능한 모든 경우 찾기
    for a in range(len(core[0])):
        temp = [i[:] for i in arr]
        A = howlong(core[0][a][0],core[0][a][1],core[0][a][2],0)
        if A == False: break
        for b in range(len(core[1])):
            B = howlong(core[1][b][0], core[1][b][1], core[1][b][2], 0)
            if B == False: break
            for c in range(len(core[2])):
                C = howlong(core[2][c][0], core[2][c][1], core[2][c][2], 0)
                if C == False: break
                for d in range(len(core[3])):
                    D = howlong(core[3][d][0], core[3][d][1], core[3][d][2], 0)
                    if D == False: break
                    for e in range(len(core[4])):
                        E = howlong(core[4][e][0], core[4][e][1], core[4][e][2], 0)
                        if E == False: break
                        tempans = A+B+C+D+E
                        print(tempans)





        

