import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))
stack = [(arr[0],0)]
ans = [-1]*N
for i in range(1,N):
    if arr[i] > stack[-1][0]:
        while stack and arr[i] > stack[-1][0]:
            ans[stack.pop()[1]] = arr[i]
    stack.append((arr[i],i))

print(*ans)
