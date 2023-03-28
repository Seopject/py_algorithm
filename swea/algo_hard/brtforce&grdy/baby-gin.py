def is_valid(list):
    if list[0] == list[1] == list[2]:
        return True

    elif list[0] == list[1]-1 == list[2]-2:
        return True


def babyjin(i,N):
    global result
    if i == N:

        partA = ans[0:3]
        partB = ans[3:7]

        if is_valid(partA) == is_valid(partB) == True:
            result = 'babyjin'
            return

    else:
        for j in range(6):
            if visited[j] == 0:
                ans[i] = num[j]
                visited[j] = 1
                babyjin(i+1,N)
                visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input()))
    visited = [0]*6
    ans = [0]*6
    result = 'Lose'
    babyjin(0,6)
    print(f'#{tc} {result}')
