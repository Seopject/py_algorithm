N, M, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)][::-1]
for a in range(N-D+1):
    temp = arr[a:a+D]
    for i in range(D):
        print(temp[i])
    print()