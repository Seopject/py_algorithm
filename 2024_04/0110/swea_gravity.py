T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    maxVal = 0
    for i in range(N-1):
        temp = 0
        for j in range(i+1,N):
            if numbers[i] > numbers[j]:
                temp += 1
        maxVal = max(temp, maxVal)
    print(f'#{tc} {maxVal}')
