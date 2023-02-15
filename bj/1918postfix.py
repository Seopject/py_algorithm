# tc = B*(A+B)-C+(A-C*(A+B))
arr = list(input())
stack = []
temp = ''
instack = {'(' : 0,'+':1 ,'-':1 ,'*':2 ,'/':2}
top = -1
# 후위로 바꾸기
for i in range(len(arr)):
    if arr[i] == ')':
        while stack[-1] != '(':
            temp += stack.pop()
            top -= 1
        stack.pop()
        top -= 1
    elif arr[i] == '(':
        stack.append('(')
        top += 1
    elif arr[i] not in instack:
        temp += arr[i]
    else:
        if top == -1:
            stack.append(arr[i])
            top += 1
        # 우선순위에 따라 변경
        elif instack[stack[-1]] < instack[arr[i]]:
            stack.append(arr[i])
            top += 1

        elif instack[stack[-1]] >= instack[arr[i]]:
                while top >= 0:
                    if not stack:
                        break
                    else:
                        temp += stack.pop()
                        top -= 1
                stack.append(arr[i])
                top += 1
while stack:
    temp += stack.pop()
print(temp)