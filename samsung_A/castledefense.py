import sys
from collections import deque
input = sys.stdin.readline

def combi(idx,list):    # 조합 재귀
    if len(list) == v:
        archer.append(list[:])
        return
    for i in range(idx,M):
        combi(i+1,list+[choose[i]])

N, M, D = map(int,input().rstrip().split())
arr = [list(map(int,input().rstrip().split())) for _ in range(N)][::-1]
choose = list(range(M))
archer = []     # 아처가 있을 수 있는 열
v = 3   # 3열에만 설 수 있음
combi(0,[])     # 궁수 3명이 서는 모든 조합

maxV = 0    # 제거하는 적의 최대 값
for m in range(len(archer)):    # 서는 경우마다 계산
    kill = []
    for k in range(N):
        for arch in archer[m]:
            target = (99999, 99999)  # 거리, 열
            target_long = 99999
            for i in range(k,N):    # 배열 검사
                if i >= D+k: break # for i
                for j in range(M):
                    if arr[i][j] == 1:
                        r,c = i-k,j     # 타겟 좌표
                        x,y = -1,arch   # 궁수 좌표
                        distance = abs(r-x) + abs(c-y)      # 최대한 가깝고 왼쪽우선
                        if distance <= D:
                            if target_long == distance and c < target[1]:
                                target = (i,j)
                                target_long = distance
                            elif target_long > distance:
                                target = (i,j)
                                target_long = distance

            if target not in kill and target != (99999,99999):
                kill.append(target)

    if len(kill) > maxV:
        maxV = len(kill)

print(maxV)