# N : 직사각형 수, K : 색칠할 사각형 수
# N개중 K개를 색칠하고, 색칠된 영역의 최대값
# 사각형 겹칠 수 있고, 겹칠 경우 해당 영역 중 가장 높은 번호를 가진 직사각형만 보인다
N,K = map(int,input().split())
box = [0]*N
for n in range(N):
    box[n] = list(map(int,input().split()))
    # [[1, 1, 5, 3], [3, 2, 7, 4], [2, 5, 9, 7]]
    # x1,y1,x2,y2 (왼쪽 아래, 오른쪽 위 좌표)

# 음수 좌표 처리( 나중에 꼭 하기ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ)
'''
for i in range(len(box)):
    for j in range(len(box[i])):
        box[i][j] += 10000
'''

# 크기 같다면 먼저 들어온게 우선순위
# 나중에 들어온게 가림
# 가려진 크기도 고려

# 나중에 범위 수정하기
arr = [[0]*15 for _ in range(15)]
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
    for i in range(15):
        cnt[b][1] += arr[i].count(b+1)

for i in range(15):
    print(arr[i])

ans = [0]*K
cnt.sort(key=lambda x:x[-1], reverse=True)
for i in range(K):
    ans[i] = cnt[i][0]
print(*sorted(ans))
