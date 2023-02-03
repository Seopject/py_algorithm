N = int(input())
numlist = [0]*N
for i in range(N):
    numlist[i] = int(input())

numlist.sort()
for i in range(N):
    print(numlist[i])