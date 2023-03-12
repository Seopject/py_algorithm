from collections import deque

T = int(input())
for tc in range(T):
    N, ansidx = map(int,input().split())
    arr = list(map(int,input().split()))
    tarr = [0]*len(arr)
    for i in range(len(arr)):
        tarr[i] = [arr[i],i]

    Q = deque(tarr)

    target = Q[ansidx]
    cnt = 0
    while Q:
        temp = Q[0]
        for i in range(1,len(Q)):
            if temp[0] < Q[i][0]:
                Q.append(Q.popleft())
                break # for i

        else:
            cnt += 1
            Q.popleft()
            if temp[1] == ansidx:
                print(cnt)
                break # while