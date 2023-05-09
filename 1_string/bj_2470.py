N = int(input())
arr = list(map(int,input().split()))
temp = 900000000
for i in range(N//2):
    for j in range(i+1,N):
        temp = min(temp, abs(arr[i]+arr[j]))

print(temp)