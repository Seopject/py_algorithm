T = 10
for tc in range(1,T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2,N-2):
        # 빌딩 최대값
        minVal = 255
        for j in range(i-2,i+3):
            # 가운데 패스
            if j == i: pass
            # 좌우 검사
            elif buildings[i] - buildings[j] > 0:
                minVal = min(buildings[i]-buildings[j], minVal)
            else:
                # 안되면 패스
                minVal = 0
                break
        ans += minVal
    print(f'#{tc} {ans}')




