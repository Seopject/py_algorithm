txt = input()
stack = [0]*len(txt)
top = -1
for x in txt:
    top += 1
    if x == '(':
        stack[top] = '('
    elif x == ')':
        