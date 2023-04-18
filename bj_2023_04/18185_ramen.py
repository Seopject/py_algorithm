import sys
input = sys.stdin.readline

N = int(input())
dp = list(map(int,input().rstrip().split())) + [0,0]

ans = 0
for i in range(N):
    if dp[i+1] > dp[i+2]:
        temp1 = min(dp[i],dp[i+1]-dp[i+2])
        dp[i] -= temp1
        dp[i + 1] -= temp1
        ans += temp1 * 5

        temp2 = min(dp[i], dp[i+1], dp[i+2])
        dp[i] -= temp2
        dp[i+1] -= temp2
        dp[i+2] -= temp2
        ans += temp2 * 7

    else:
        temp3 = min(dp[i], dp[i+1], dp[i+2])
        dp[i] -= temp3
        dp[i + 1] -= temp3
        dp[i + 2] -= temp3
        ans += temp3 * 7

        temp4 = min(dp[i], dp[i + 1])
        dp[i] -= temp4
        dp[i + 1] -= temp4
        ans += temp4 * 5

    ans += dp[i]*3

print(ans)
