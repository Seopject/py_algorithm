txt = input()
bomb = list(input())
stack = []
top = -1
for strn in txt:
    stack.append(strn)
    top += 1
    if stack[top-len(bomb)+1:top+1] == bomb:
        for t in range(len(bomb)):
            stack.pop()
            top -= 1
if not stack:
    print('FRULA')
else:
    print(''.join(stack))
