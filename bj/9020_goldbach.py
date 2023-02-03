T = int(input()) # tc
for tc in range(T):
    n = int(input())
    
    # n까지의 소수 찾기
    prime = [True, True] + [False]*(n-1)
    for i in range(2,int(n**1/2)):
        if prime[i] == False:
            for j in range(i*2,n,i):
                prime[j] = True
    
    # n까지 소수 저장
    findprime = []
    for k in range(n):
        if prime[k] == False:
            findprime.append(k)

    answer = [0]*2
    # n-소수를 한 값이, 소수 리스트에 있다면 답에 저장
    for i in range(len(findprime)):
        temp = n - findprime[i]
        if (temp in findprime) and (temp*findprime[i] > answer[1]*answer[0]):
            answer = findprime[i],temp
    # 다수의 답에서 가장 차이가 적은 값 출력
    print(*answer)