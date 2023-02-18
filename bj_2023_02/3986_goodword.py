N = int(input())
cnt = 0
for n in range(N):
    txt = list(input())
    stack = []
    for i in range(len(txt)):
        if not stack or stack[-1] != txt[i]:
            stack.append(txt[i])
        elif stack and stack[-1] == txt[i]:
            stack.pop()
    if not stack:
        cnt += 1

print(cnt)