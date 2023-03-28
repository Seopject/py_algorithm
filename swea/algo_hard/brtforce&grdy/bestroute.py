def samsung_joah(i,N):
    global result

    if i == N:

        temp = 0
        for k in range(N-1):
            temp += abs(answer[k][0] - answer[k+1][0])
            temp += abs(answer[k][1] - answer[k+1][1])
        temp += abs(samsung[0] - answer[0][0])
        temp += abs(samsung[1] - answer[0][1])
        temp += abs(answer[N-1][0] - home[0])
        temp += abs(answer[N-1][1] - home[1])

        if result > temp:
            result = temp

    else:
        for j in range(N):
            if visited[j] == 0:
                answer[i] = clients[j]
                visited[j] = 1
                samsung_joah(i+1,N)
                visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 고객의 수
    arr = list(map(int,input().split()))

    # 샘숭
    samsung = (arr[0],arr[1])
    # 집은 가야죠..
    home = (arr[2],arr[3])
    clients = []
    # 고객님
    for i in range(2, N+2):
        clients.append((arr[2*i],arr[2*i+1]))
    visited = [0]*N
    answer = [0]*N
    result = 99999999
    samsung_joah(0,N)
    print(f'#{tc} {result}')