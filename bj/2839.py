N = int(input()) # 설탕의 무게
x = N//5
y = N//3
test = []
answer = []

if N%5 == 0:
    print(N//5)
else:
    for i in range((N//5)+1):
        if (N - 5*i)%3 == 0:
            test += [((i, (N-5*i)//3))]

    if test == []:
        print(-1)

    else:
        print(sum(test[-1]))