N = int(input()) # 피연산자 개수
txt = list(input())
stack = []
do = {'+':1,'-':1,'*':2,'/':2}
num = {}
for i in range(N):
    num[chr(65+i)] = int(input())

for i in range(len(txt)):
    if txt[i] not in do:
        stack.append(num.get(txt[i]))
    elif txt[i] in do:
        r2 = stack.pop()
        r1 = stack.pop()
        if txt[i] == '+':
            stack.append(r1+r2)
        elif txt[i] == '-':
            stack.append(r1-r2)
        elif txt[i] == '*':
            stack.append(r1*r2)
        elif txt[i] == '/':
            stack.append(r1/r2)
print(f'{stack[0]:.2f}')