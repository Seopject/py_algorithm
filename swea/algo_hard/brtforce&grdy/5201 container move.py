T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    weight = list(map(int, input().split()))
    ton = list(map(int,input().split()))
    answer = 0
    weight.sort(reverse=True)
    ton.sort(reverse=True)

    for i in range(M):
        for j in range(N):
            if ton[i] >= weight[j]:
                answer += weight[j]
                weight[j] = 999
                break

    print(f'#{tc} {answer}')