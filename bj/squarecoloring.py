# 1186
# N : 직사각형 수, K : 색칠할 사각형 수
# N개중 K개를 색칠하고, 색칠된 영역의 최대값
# 사각형 겹칠 수 있고, 겹칠 경우 해당 영역 중 가장 높은 번호를 가진 직사각형만 보인다
N,K = map(int,input().split())
box = [0]*N
for n in range(N):
    box[n] = list(map(int,input().split()))

minV = 10000
maxV = -10000
for i in range(len(box)):
    for j in range(len(box[i])):
        if minV > box[i][j]:
            minV = box[i][j]

for i in range(len(box)):
    for j in range(len(box[i])):
        box[i][j] += minV

until = abs(minV)+abs(maxV)+1

# 나중에 범위 수정하기
arr = [[0]*(until) for _ in range(until)]
# 박스 인덱스, 넓이
cnt = [[0,0] for _ in range(len(box))]
# 좌표 색칠
for b in range(len(box)):
    x1,y1,x2,y2 = box[b]
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            arr[i][j] = b+1
# 각 박스 인덱스와 넓이 구하기
for b in range(len(box)):
    cnt[b][0] = b+1
    for i in range((until)):
        cnt[b][1] += arr[i].count(b+1)

ans = [0]*K
cnt.sort(key=lambda x:x[-1], reverse=True)
for i in range(K):
    ans[i] = cnt[i][0]
print(*sorted(ans))
