# 미리 temp를 [[0]*100]*100하면 다같이 수정되더라
temp = []
for i in range(100):
    temp.append([0]*100)
    
N = int(input()) # 색종이 N개
for tc in range(N):
    W, H = map(int, input().split())
    for i in range(10):
        for j in range(10):
            temp[H-1+i][W-1+j] = 1

cnt = 0
for i in range(100):
    cnt += sum(temp[i])

print(cnt)