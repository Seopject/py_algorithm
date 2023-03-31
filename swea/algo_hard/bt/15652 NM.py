def func(i,M):
    if i == M:
        print(*p)
    else:
        for j in range(N):
            used = [0]*N
            if p[i] <= arr[j] and p[i-1] <= arr[j]:
                p[i] = arr[j]
                func(i+1,M)
                p[i] = 0

N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
p = [0]*M
func(0,M)