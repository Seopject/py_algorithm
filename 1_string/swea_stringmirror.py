T = int(input())
for tc in range(1,T+1):
    arr = list(input())[::-1]
    for i in range(len(arr)):
        if arr[i] == 'b':
            arr[i] = 'd'
        elif arr[i] == 'd':
            arr[i] = 'b'
        elif arr[i] == 'p':
            arr[i] = 'q'
        else:
            arr[i] = 'p'

    print(f'#{tc}',''.join(arr))