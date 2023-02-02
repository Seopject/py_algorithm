while True:
    n = int(input())
    if n == 0:
        break
    m = 2*n
    prime = [1,1] + [0]*(m-1)
    for i in range(2,int(m**1/2)+1):
        if prime[i] == 0:
            for j in range(2*i, m+1, i):
                prime[j] = 1
    # n보다 크고! 2n(m) 보다 작거나 같은!
    print(prime[n+1:m+1].count(0))
