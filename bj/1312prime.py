A,B,N = map(int,input().split())
num = list(str(round(A/B,N+2)))
ans = [0]*(N+1)
idx = num.index('.')
for i in range(idx,len(ans)):
    if i >= len(num) or len(ans):
        break
    ans[i-idx] = num[i]
print(idx)
print(num)
print(ans)
print(ans[-1])
