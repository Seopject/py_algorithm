# 내 생각
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     for i in range(N):
#         for j in range(N-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     print(f'#{tc} {numbers}')

# 최적화
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 버블 정렬은 마지막부터 채워 나간다.
    # 채운 부분은 다시 조회할 필요 없다.
    for i in range(N, 1, -1):
        for j in range(i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(f'#{tc}', *numbers)
