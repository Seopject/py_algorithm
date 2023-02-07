N = int(input())
space = [['*']*N for _ in range(N)]
def stars(n):
    global space

    if n == 1:
        for i in range(N):
            print(space[i])
    else:
        for r in range((n//3),2*(n//3)):
            for c in range((n//3),2*(n//3)):
                space[r][c] = ' '
        for k in range(3):
            for x in range((n//3)*k+(n//(3*3)),(n//3)*k+2*(n//(3*3))):
                for y in range((n//3)*k+(n//(3*3)),(n//3)*k+2*(n//(3*3))):
                    space[x][y] = ' '

        return stars(n//3)
stars(N)