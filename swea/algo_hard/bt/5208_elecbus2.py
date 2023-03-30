def func(cnt, idx,bat,N):  # cnt 교체횟수, idx 위치 인덱스, bat 위치 배터리 잔여, N 정류장수
    global minV

    if idx + bat >= N-1:
        if cnt < minV:
            minV = cnt
        return
    elif bat < 0:
        return
    elif cnt >= minV:
        return

    # 교체
    func(cnt+1,idx+1,btry[idx]-1,N)
    # 그냥 가
    func(cnt,idx+1,bat-1,N)

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    btry = arr[1:]
    minV = 99999999

    func(0,1,btry[0]-1,arr[0])

    print(f'#{tc} {minV}')