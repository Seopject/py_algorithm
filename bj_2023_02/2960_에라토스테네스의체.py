N, K = map(int,input().split())
arr = [0,0] + [1]*(N-1)
cnt = 0
ans = []
for i in range(2,N+1):
    if arr[i] == 1:
        arr[i] = 0
        cnt += 1
        if not ans and cnt == K:
            ans.append(i)
            break

    for j in range(2*i,N+1,i):
        if arr[j] == 0:
            pass
        else:
            arr[j] = 0
            cnt += 1
            if not ans and cnt == K:
                ans.append(j)
                break

print(*ans)