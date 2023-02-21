def bisearch(l,r,key,arr):
    while l <= r:
        c = (l + r)//2
        if key == arr[c]:
            return 1
        elif key < arr[c]:
            r = c-1
        elif key > arr[c]:
            l = c+1
    return 0

N = int(input())
card = sorted(list(map(int,input().split())))
M = int(input())
tc = list(map(int,input().split()))

for i in range(M):
    print(bisearch(0,N-1,tc[i],card), end = ' ')