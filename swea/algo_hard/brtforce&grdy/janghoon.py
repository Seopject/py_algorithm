def top(i,k):
    global answer, B
    if i == k:
        temp = 0
        for k in range(N):
            temp += p[k]*arr[k]
        if temp >= B and answer > temp:
            answer = temp

    else:
        p[i] = 0
        top(i+1,k)
        p[i] = 1
        top(i+1,k)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = 2000001
    visited = []
    p = [0]*N

    top(0, N)

    print(f'#{tc} {answer - B}')