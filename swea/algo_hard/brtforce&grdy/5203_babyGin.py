def runn(list):
    for i in range(8):
        if list[i] >= 1 and list[i+1] >= 1 and list[i+2] >= 1:
            return True

# 0 1 2 3 4 5 6 7 8 9

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    # 0~9 count arr
    cntA = [0]*10
    cntB = [0]*10

    answer = 0

    for i in range(6):
        cntA[arr[2 * i]] += 1
        if cntA[arr[2*1]] == 3 or runn(cntA) == True:
            answer = 1
            break

        cntB[arr[2 * i + 1]] += 1
        if cntB[arr[2*i+1]] == 3 or runn(cntB) == True:
            answer = 2
            break

    print(f'#{tc} {answer}')