# 백트래킹
def f(i,k,s,key,rs):
    global cnt

    if s == key:
       cnt += 1
       return
    elif i==k or s>key or s+rs<key:
        return
    # if i == k:
    #     if s == key:
    #         cnt += 1

    else:
        f(i+1,k,s,key, rs - A[i])
        f(i+1,k,s+A[i],key, rs-A[i])
        return


A = [i for i in range(1,11)]
N = 10
bit = [0]*N
cnt = 0
key = 10
f(0,N,0,key,sum(A))
print(cnt)