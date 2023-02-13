#2167번
N, M = map(int,input().split()) # NxM의 배열
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
area = [[0]]*K
for i in range(K):
    area[i] = (list(map(int,input().split())))

for k in range(len(area)):
    x1,y1,x2,y2 = area[k]
    ans = 0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            ans += arr[i][j]
    print(ans)