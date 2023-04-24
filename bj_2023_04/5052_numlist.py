import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    arr.sort()
    for i in range(N-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print('NO')
            break
    else:
        print('YES')