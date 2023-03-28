def combinations(n,r,s):    # n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            combinations(n,r-1,i+1)



n = 10
r = 3
comb = [0]*3
A = [i for i in range(n)]
combinations(n,r,0)