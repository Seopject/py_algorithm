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
inarr = [list(map(int,input().rstrip().split())) for _ in range(N)][::-1]
choose = list(range(M))
archer = []     # 아처가 있을 수 있는 열
v = 3   # 3개의 열에만 설 수 있음
combi(0,[])     # 궁수 3명이 서는 모든 조합 생성 -> archer

maxV = 0    # 제거하는 적의 최대 값
for m in range(len(archer)):    # 서는 경우마다 계산
    arr = [t[:] for t in inarr]
    kill = []
    for k in range(N):
        if kill:
            for t in range(len(kill)):
                r, c = kill[t]
                arr[r][c] = 0
        for arch in archer[m]:
            target = deque([])
            for i in range(k,N):    # 배열 검사
                if i >= D+k: break # for i
                for j in range(M):
                    if arr[i][j] == 1:
                        r,c = i-k,j     # 타겟 좌표
                        x,y = -1,arch   # 궁수 좌표
                        distance = abs(r-x) + abs(c-y)      # 최대한 가깝고 왼쪽우선
                        if distance <= D:
                            if not target:
                                target.append((i,j,distance))
                            elif distance == target[0][2]:
                                if j < target[0][1]:
                                    target.appendleft((i,j,distance))
                            elif distance < target[0][2]:
                                target.appendleft((i,j,distance))
            if target and target[0][:2] not in kill:
                kill.append(target[0][:2])

    if len(kill) > maxV:
        maxV = len(kill)

print(maxV)