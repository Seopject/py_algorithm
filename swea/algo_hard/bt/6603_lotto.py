def lottogaza(i,F,idx):
    if i == 6:
        print(*p)

    else:
        for j in range(idx+1, k):
            p[i] = arr[j]
            lottogaza(i+1,F,j)


while True:
    _input = list(map(int,input().split()))
    if _input == [0]: break     # 종료 조건

    k = _input[0]
    arr = _input[1:]
    p = [0] * 6
    lottogaza(0,6,-1)
    print()
