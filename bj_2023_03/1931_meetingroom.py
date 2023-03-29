import sys

N = int(input())
arr = [0]*N
for n in range(N):
    s, e = map(int,sys.stdin.readline().rstrip().split())
    arr[n] = (s,e)

arr.sort(key=lambda x:(x[1], x[0]))
answer = 1
target = 0
for i in range(1,N):
    if arr[i][0] >= arr[target][1]:
        target = i
        answer += 1

print(answer)