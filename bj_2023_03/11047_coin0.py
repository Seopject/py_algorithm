N, K = map(int,input().split())
arr = []
for i in range(N):
    temp = int(input())
    if temp > K:
        break
    else:
        arr.append(temp)

arr.sort(reverse=True)
idx = 0
tempvalue = 0
tempK = K
ans = 0
while tempvalue != K:
    t= 0
    t = tempK//arr[idx]
    if t != 0:
        ans += t
        tempvalue += t*arr[idx]
        tempK -= t*arr[idx]
        idx += 1
    else:
        idx+=1
print(ans)
