import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))[::-1]
stack = [(arr[0],0)]
ans = [0]*N
for i in range(1,N):
    if arr[i] > stack[-1][0]:
        while stack and arr[i] > stack[-1][0]:
            ans[stack.pop()[1]] = N-i
    stack.append((arr[i],i))

print(*ans[::-1])