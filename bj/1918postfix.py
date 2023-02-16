# tc = (C+B*(C+B)*(C*B)-B)
arr = list(input())
stack = []
temp = ''
instack = {'(' : 0,'+':1 ,'-':1 ,'*':2 ,'/':2}
outstack = {'(' : 3,'+':1 ,'-':1 ,'*':2 ,'/':2}
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
        stack.append(arr[i])
        top += 1
    elif arr[i] not in instack:
        temp += arr[i]
    elif top == -1:
        stack.append(arr[i])
        top += 1
    elif instack[stack[-1]] < instack[arr[i]]:
        stack.append(arr[i])
        top += 1
    elif outstack[stack[-1]] >= outstack[arr[i]]:
        while top >= 0 and instack[stack[-1]] >= instack[arr[i]]:
            temp += stack.pop()
            top -= 1
        stack.append(arr[i])
        top += 1


while stack:
    temp += stack.pop()
print(temp)