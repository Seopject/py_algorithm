def bit(i,N):
    global answer

    if i == N:
        temp = 0
        for n in range(N):
            temp += arr[n]*p[n]
        if temp == K:
            answer += 1
    else:
        p[i] = 0
        bit(i+1,N)
        p[i] = 1
        bit(i+1,N)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = 0
    p = [0]*N

    if sum(arr) < K:
        print(f'#{tc} {answer}')
        continue
    elif sum(arr) == K:
        answer = 1
        print(f'#{tc} {answer}')
        continue

    bit(0,N)


    print(f'#{tc} {answer}')