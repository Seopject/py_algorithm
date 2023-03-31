def func(i,cost):
    global answer

    if i >= 12:
        answer = min(cost,answer)

    elif cost >= answer: return

    else:
        func(i+1,cost + arr[i])  # Day cost & Month
        func(i+3,cost + M3)         # 3 Month
        func(i+12, cost + Y)        # Year

T = int(input())
for tc in range(1,T+1):
    D, M, M3, Y = map(int,input().split())
    arr = list(map(int,input().split()))

    for i in range(12):
        if arr[i]*D > M:
            arr[i] = M
        else:
            arr[i] *= D

    answer = 3000*366

    func(0,0)

    print(f'#{tc} {answer}')
