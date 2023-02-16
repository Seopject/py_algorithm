import sys
input = sys.stdin.readline
N = int(input())
top = list(map(int,input().rstrip().split()))
stack = [0]*N
for i in range(N-1,-1,-1):
    temp = i
    while temp >-1:
        temp -= 1
        if top[i] < top[temp]:
            stack[i] = temp+1
            break
    else:
        stack[i] = 0
print(*stack)