N = int(input()) # 만들어진 수
M = N
ans = 0
while M>0:
    M -= 1
    Mtemp = M
    M = list(str(M))
    for i in range(len(M)):
        M[i] = int(M[i])
    if sum(M) + Mtemp == N:
        ans = Mtemp
        M = Mtemp
    else:
        M = Mtemp

print(ans)