T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_num = 1000000
    max_num = 0

    for i in range(N):
        if min_num > numbers[i]:
            min_num = numbers[i]
        elif max_num < numbers[i]:
            max_num = numbers[i]

    print(f'#{tc} {max_num - min_num}')
