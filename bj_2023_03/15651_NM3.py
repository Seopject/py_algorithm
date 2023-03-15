from itertools import product

N, M = map(int,input().split())
arr = list(range(1,N+1))

for i in product(arr,repeat=M):
    print(*i)