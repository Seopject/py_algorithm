# N까지 소수 구하기
# 1)0~N까지의 배열 만들기 ([0] * (N+1))
# i의 범위 2 ~ 루트N
# i부터 루트N 전의 i배수 전부 1로
# 다음 1이 아닌 요소 찾아서 반복

N = int(input())
test = [1,1]+[0]*(N-1)
prime = []

for i in range(2, int(N**1/2)+1):
    if test[i] != 1:
        for j in range(i+i,N+1,i):
            test[j] = 1

for k in range(len(test)):
    if test[k] == 0:
        print(k)
