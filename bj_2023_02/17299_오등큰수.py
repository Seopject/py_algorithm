N = int(input())
arr = list(map(int,input().split()))
cnt = [0]*10000001
for i in range(N):
    cnt[arr[i]] += 1
stack = []
ans = [-1]*N
for i in range(N):
    if not stack:
        stack.append(i)
    elif cnt[arr[stack[-1]]] < cnt[arr[i]]:
        while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
            ans[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
    elif cnt[arr[stack[-1]]] >= cnt[arr[i]]:
        stack.append(i)
print(*ans)