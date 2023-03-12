arr = list(input())
cnt = [[0,'+'] for _ in range(50)]
stack = []
idx = -1

ans = 0
calc = 0
for temp in arr:
    if temp == '(':
        idx += 1
        if not stack:
            stack.append(temp)
            cnt[idx][0] = 2
        else:
            stack.append(temp)
            cnt[idx-1][1] ='*'
            cnt[idx][0] = 2

    elif temp == '[':
        idx += 1
        if not stack:
            stack.append(temp)
            cnt[idx][0] = 3
        else:
            stack.append(temp)
            cnt[idx-1][1] = '*'
            cnt[idx][0] = 3


    elif temp == ')':
        if stack[-1] != '(':
            print(0)
            break
        else:
            if cnt[idx][1] == '+':
                calc += 2
                stack.pop()
                cnt[idx] = [0,'+']
                idx -= 1
            elif cnt[idx][1] == '*':
                cnt[0][2] *= 2
                stack.pop()
                cnt[idx] = [0, '+']
                idx -= 1

    elif temp == ']':
        if stack[-1] != '[':
            print(0)
            break
        else:
            if cnt[idx][1] == '+':
                cnt[0][2] += 3
                stack.pop()
                cnt[idx] = [0,'+']
                idx -= 1
            elif cnt[idx][1] == '*':
                cnt[0][2] *= 3
                stack.pop()
                cnt[idx] = [0, '+']
                idx -= 1
    if idx < 0:
        ans += cnt[0][2]
        cnt[0] = [0,'+']

print(ans)