origin = list(input())
target = list(input())

while target:
    if origin == target:
        print(1)
        break
    elif len(target) <= len(origin):
        print(0)
        break

    if target[-1] == 'A':
        target.pop()
    elif target[-1] == 'B':
        target.pop()
        target = target[::-1]

else:
    print(0)