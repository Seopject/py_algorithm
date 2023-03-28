T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0]*N
    p = [0]*N
    answer = 1
    for n in range(N):
        s, e = map(int,input().split())
        arr[n] = (s,e)

    arr.sort(key=lambda x: x[1])

    target = 0
    for i in range(1,N):
        if arr[i][0] >= arr[target][1]:
            answer += 1
            target = i

    print(f'#{tc} {answer}')