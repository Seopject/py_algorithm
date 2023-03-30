T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    target = list(map(int,input().split()))
    answer = 0

    for i in range(M):
        t = target[i]
        l, r = 0, N-1
        LRtemp = []

        while l<=r:
            m = (l+r) // 2
            if A[m] == t:
                answer += 1
                break

            elif A[m] > t:
                r = m-1
                if LRtemp and LRtemp[-1] == 'L': break
                else:
                    LRtemp.append('L')

            elif A[m] < t:
                l = m+1
                if LRtemp and LRtemp[-1] == 'R': break
                else:
                    LRtemp.append('R')

    print(f'#{tc} {answer}')

