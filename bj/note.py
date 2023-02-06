def max_value(arr):
    maxV = 1
    for i in range(len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
    return maxV

T = int(input())
total_arr = []
for test_case in range(1, T+1):

    N = int(input())
    for _ in range(N):
        arr = list(map(int, input().split()))
        start = arr[1]          # 처음 정류장
        end = arr[2]            # 마지막 정류장

        if arr[0] == 1:         # 구간 사이 모든 정류장
            for i in range(start, end + 1):
                total_arr.append(i)

        elif arr[0] == 2:       # 홀이면 홀 짝이면 짝
            for i in range(start, end + 1, 2):
                total_arr.append(i)
            if end not in total_arr:
                total_arr.append(end)

        elif arr[0] == 3:
            if start % 2 == 0:
                for i in range(start, end + 1):
                    if i % 4 == 0 and i % 10 != 0:
                        total_arr.append(i)
                    elif i == start or i == end:    # 처음, 마지막 정류장 포함
                        total_arr.append(i)
            else:
                for i in range(start, end + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        total_arr.append(i)
                    elif i == start or i == end:    # 처음, 마지막 정류장 포함
                        total_arr.append(i)

    counts = [0] * (max_value(total_arr)+1)

    for i in range(len(total_arr)):
        counts[total_arr[i]] += 1

    print(counts)

    print(f'#{test_case}', max_value(counts))