try:
    A,B,N = map(int,input().split())
    ans = list(str(round(A/B,N+1)))
    print(ans[ans.index('.')+N])
except:
    IndexError
    print(0)