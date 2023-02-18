N = int(input()) # 빌딩개수
stack = []
cnt = 0
for i in range(N):
    h = int(input())
    if not stack:
        stack.append(h)
    elif stack[-1] > h:
        cnt += len(stack)
        stack.append(h)
    elif stack[-1] <= h:
        while stack and stack[-1] <= h:
            stack.pop()
        cnt += len(stack)
        stack.append(h)

print(cnt)