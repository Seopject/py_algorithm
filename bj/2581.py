M = int(input())
N = int(input())

answer = []

for i in range(M,N+1):
    check = []
    for j in range(1, int(i**1/2)+1):
        if i % j == 0:
            check.append(j)
    if len(check) == 1:
        answer.append(i)

if answer == []:
    print(-1)

else:
    print(sum(answer))
    print(answer[0])