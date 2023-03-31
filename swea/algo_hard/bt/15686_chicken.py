def combi(i,M,idx):
    global ans

    if i == M:
        tempans = 0
        for a in range(len(homes)):
            hx, hy = homes[a]
            temp = 999
            for b in range(len(p)):
                temp = min(temp, abs(p[b][0]-hx) + abs(p[b][1]-hy))
            tempans += temp
        ans = min(tempans, ans)

    else:
        for j in range(idx+1,len(stores)):
            p[i] = stores[j]
            combi(i+1,M,j)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

homes = []
stores = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i,j))
        elif arr[i][j] == 2:
            stores.append((i,j))

ans = 99999999
p = [0]*M
combi(0,M,-1)

print(ans)