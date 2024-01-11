T = 10
for tc in range(1,T+1):
    case = int(input())
    arr = [0]*100
    maxVal = 0

    # 가로 최대
    for i in range(100):
        arr[i] = list(map(int, input().split()))
        if sum(arr[i]) > maxVal:
            maxVal = sum(arr[i])

    # 세로 최대
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
            if maxVal < temp:
                maxVal = temp

    # 대각선 최대
    temp1 = 0
    temp2 = 0
    for i in range(100):
        temp1 += arr[i][i]
        temp2 += arr[99-i][i]
    maxVal = max(maxVal, temp1, temp2)

    print(f'#{tc} {maxVal}')