M, N = map(int, input().split())

prime = [1,1] + [0]*(N-1)
for i in range(2, int(N**1/2)+1):
    if prime[i] == 0:
        for j in range(2*i,N+1,i):
            prime[j] = 1

for k in range(M,N+1):
    if prime[k] == 0:
        print(k)