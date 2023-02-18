N, M, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split()))

for t in range(R):
    # 1
    if order[t] == 1:
        arr = arr[::-1]
    # 2
    elif order[t] == 2:
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
    # 3
    elif order[t] == 3:
        arr = list(map(list, zip(*arr[::-1])))
    # 4
    elif order[t] == 4:
        arr = list(map(list, zip(*arr)))[::-1]
    # 5
    elif order[t] == 5:
        # 리스트 세로 절반
        for i in range(len(arr)):
            arr[i][:len(arr[i])//2], arr[i][len(arr[i])//2:] = arr[i][len(arr[i])//2:], arr[i][:len(arr[i])//2]
        # 대각선 교차
        for i in range(len(arr)//2):
            arr[i][:len(arr[i])//2], arr[len(arr)//2+i][len(arr[i])//2:] = arr[len(arr)//2+i][len(arr[i])//2:], arr[i][:len(arr[i])//2]
    # 6
    elif order[t] == 6:
        # 리스트 세로 절반
        for i in range(len(arr)):
            arr[i][:len(arr[i]) // 2], arr[i][len(arr[i]) // 2:] = arr[i][len(arr[i]) // 2:], arr[i][:len(arr[i]) // 2]
        # 대각선 교차
        for i in range(len(arr)//2):
            arr[i][len(arr[i])//2:], arr[len(arr)//2+i][:len(arr[i])//2] = arr[len(arr)//2+i][:len(arr[i])//2], arr[i][len(arr[i])//2:]

for i in range(len(arr)):
    print(*arr[i])