N = int(input())
stack = [0]*N
for i in range(N):
    x,y = map(int,input().split())
    stack[i] = [x,y]
stack.sort(key = lambda x:x[0] and x[1], reverse=True)

temp = 1
ans = [0]*N
for i in range(N):
    if stack[i][0] > stack[i+1][0] and s





print(stack)