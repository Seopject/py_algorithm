# SWEA 4835 - 1일차 - 구간합
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    low_value = 10000*N
    max_value = 0
    for i in range(N-M+1):
        temp_value = sum(numbers[i:i+M])
        low_value = min(low_value, temp_value)
        max_value = max(max_value, temp_value)
    print(f'#{tc+1} {max_value - low_value}')