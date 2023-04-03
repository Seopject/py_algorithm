import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
dp = [0]*(N+1)

# 1
dp[1] = 3*A[1]
# 2
if N >= 2:
    dp[2] = min(dp[1]+(3*A[2]), 5*min(A[1],A[2])+3*abs(A[1]-A[2]))
# 3 이후
if N >= 3:
    for i in range(3,N+1):
        dp[i] = min(
            dp[i-1]+(3*A[i]),
            dp[i-2]+(3*A[i-1])+(3*A[i]),
            dp[i-2]+5*min(A[i-1],A[i])+3*abs(A[i-2]-A[i-1]),
            7*min(A[1],A[2],A[3]) + 5*(min(A[1],A[2]) - min(A[1],A[2],A[3])) + 3*abs(A[1]-A[2])
            # 7 * min(A[1], A[2], A[3]) + 5 * (min(A[2], A[3]) - min(A[1], A[2], A[3])) + 3 * abs(A[2] - A[3])

        )
print(dp)
print(dp[N])
