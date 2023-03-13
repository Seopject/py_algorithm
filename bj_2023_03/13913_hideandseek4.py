from collections import deque

N, K = map(int,input().split())
arr = [0]*100001
arr[N] = 1  # 수빈
Q = deque([N])

time = 0
route = []

while Q:
    t = Q.popleft()
    route.append(t)
    if t == K:
        print(arr[t]-1)
        print(Q)
    if 0<=2*t<=100000 and arr[2*t] == 0:
        Q.append(2*t)
        arr[2*t] = arr[t] + 1
    if 0<=t-1<=100000 and arr[t-1] == 0:
        Q.append(t-1)
        arr[t-1] = arr[t] + 1
    if 0<=t+1<=100000 and arr[t+1] == 0:
        Q.append(t+1)
        arr[t+1] = arr[t] + 1

print(route)