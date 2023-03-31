def combi(i,N,idx):
    global ans

    if i == N//2:
        q = []
        for tmp in num:
            if tmp not in p:
                q.append(tmp)
        start = 0
        link = 0

        for s in p:
            for a in p:
                start += arr[s][a]

        for l in q:
            for b in q:
                link += arr[l][b]

        ans = min(ans,abs(start-link))

    else:
        for j in range(idx+1,N):
            p[i] = num[j]
            combi(i+1,N, j)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
p = [0]*(N//2)
num = [i for i in range(N)]
ans = 99999999

combi(0,N,-1)

print(ans)