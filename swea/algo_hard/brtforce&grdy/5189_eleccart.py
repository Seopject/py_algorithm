def perm(N, ans):
    global result

    if len(ans) == N:
        temp = 0
        for i in range(len(ans)-1):
            temp += arr[ans[i]-1][ans[i+1]-1]
        temp += arr[ans[-1]-1][0]
        if temp < result:
            result = temp


    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                ans.append(j+1)
                perm(N,ans)
                visited[j] = 0
                ans.pop()


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    ans = [1]
    result = 99999999
    perm(N,ans)
    print(f'#{tc} {result}')