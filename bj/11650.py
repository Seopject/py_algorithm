N = int(input())
xylist = [0]*N
for i in range(N):
    xylist[i] = list(map(int, input().split()))
xylist.sort()
for i in range(N):
    print(*xylist[i])