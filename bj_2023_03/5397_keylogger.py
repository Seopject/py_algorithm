T = int(input())
for tc in range(T):
    arr = list(input())
    stackL = []
    stackR = []

    for i in range(len(arr)):
        if arr[i] == '<':
            if stackL:
                stackR.append(stackL.pop())

        elif arr[i] == '>':
            if stackR:
                stackL.append(stackR.pop())

        elif arr[i] == '-':
            if stackL:
                stackL.pop()

        else:
            stackL.append(arr[i])

    while stackR:
        stackL.append(stackR.pop())

    print(''.join(stackL))
