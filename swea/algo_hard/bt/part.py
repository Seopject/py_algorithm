def bit(i, ans):
    global answer

    if ans > K: return

    if i == N:
        if ans == K:
            answer += 1
    else:
        bit(i+1,ans+arr[i])
        bit(i+1,ans)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0

    bit(0, 0)

    print(f'#{tc} {answer}')