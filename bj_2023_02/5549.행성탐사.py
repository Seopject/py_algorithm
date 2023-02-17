import sys
input = sys.stdin.readline

R, C = map(int,input().rstrip().split())
K = int(input())

arr = [list(input().rstrip()) for _ in range(R)]
for tc in range(K):
    ans = [0, 0, 0]  # J O I
    r1, c1, r2, c2 = map(int,input().rstrip().split())
    for i in range(r1-1,r2):
        ans[0] += arr[i][c1-1:c2].count('J')
        ans[1] += arr[i][c1 - 1:c2].count('O')
        ans[2] += arr[i][c1 - 1:c2].count('I')

    print(*ans)