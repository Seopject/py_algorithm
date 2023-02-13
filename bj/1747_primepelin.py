X = int(input())
N = 1003002
arr = [0,0] + [1]*(N-1)
for i in range(2,int(N**1/2)+1):
    for j in range(2*i,N+1,i):
        arr[j] = 0

for i in range(X,N):
    if arr[i] == 1 and str(i) == str(i)[::-1]:
        print(i)
        break