def top(arr, idx):
    global B, answer

    if sum(arr) == 0:
        return

    elif sum(arr) >= B and sum(arr) < answer:
        answer = sum(arr)

    for i in range(idx, N):
        temp = arr[i]
        arr[i] -= temp
        print(arr)
        print(visited)
        if arr not in visited:
            visited.append(arr)
            top(arr,i)
            arr[i] += temp
            top(arr, i)
        else:
            return

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = 2000001
    visited = []
    if sum(arr) == B:
        print(f'#{tc} {0}')
        continue

    top(arr, N)

    print(f'#{tc} {answer-B}')