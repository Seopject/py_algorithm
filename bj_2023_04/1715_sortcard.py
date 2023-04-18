N = int(input())
arr = [0]*100001
for i in range(N):
    arr[int(input())] = 1

ans = 0
for i in range(100001):
    if arr[i] != 0:
        ans += ans + i*arr[i]

print(ans)