N, M = map(int,input().split())
nolisten = set([])
dbj = []
nolook = []
for i in range(N):
    nolisten.add(input())

cnt = 0
for i in range(M):
    temp = input()
    if temp in nolisten:
        cnt += 1
        dbj.append(temp)

print(cnt)
dbj.sort()
for i in range(len(dbj)):
    print(dbj[i])