N = int(input())
space = [['*']*N for _ in range(N)]
def stars(N,x,space):
    if x == 1:
        for i in range(N):
            print(''.join(space[i]))
    else:
        temp = []
        for k in range(N//x):
            for t in range(x*k+x//3,x*(k+1)-x//3):
                temp.append(t)
        for i in range(len(temp)):
            for j in range(len(temp)):
                space[temp[i]][temp[j]] = ' '
        return stars(N,x//3,space)
stars(N,N,space)