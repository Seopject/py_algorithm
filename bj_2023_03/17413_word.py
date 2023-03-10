brkt = ['<','>']

S = list(input())
ans = ''
stack = []
status = 0
for i in range(len(S)):
    t = S[i]
    if status == 1 and t not in brkt:
        ans += t
    elif t == '<':
        if stack:
            while stack:
                ans += stack.pop()
        status += 1
        ans += t
    elif t == '>':
        status -= 1
        ans += t

    elif status == 0 and t == ' ':
        while stack:
            ans += (stack.pop())
        ans += t

    elif status == 0 and t not in brkt:
        stack.append(t)

while stack:
    ans += stack.pop()

print(ans)

