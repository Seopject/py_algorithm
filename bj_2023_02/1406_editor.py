stack1 = list(input())
stack2 = []
for m in range(int(input())):
    order = input().split()

    if order[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    elif order[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    elif order[0] == 'B' and stack1:
        stack1.pop()
    elif order[0] == 'P':
        stack1.append(order[1])

print(''.join(stack1)+''.join(stack2[::-1]))