import sys
input = sys.stdin.readline
def runaway(maze,i,j):
    rule = { 'U' : (-1,0), 'R' : (0,1), 'D' : (1,0), 'L' : (0,-1)}
    visited = []
    while True:
        # 이미 지나가서 판별된 루트
        if maze[i][j] == 'P':
            return 1
        elif maze[i][j] == 'F':
            return 0
        # 스택
        visited.append((i,j))
        # 방향
        ni,nj = i+rule.get(maze[i][j])[0], j+rule.get(maze[i][j])[1]
        # 나가거나 이미 갔던 곳 + 성공이면 P
        if ni<0 or ni>N-1 or nj<0 or nj>M-1 or maze[ni][nj] == 'P':
            while visited:
                a, b = visited.pop()
                maze[a][b] = 'P'
            return 1
        # 못나가거나 이미 실패했던 곳이면
        elif maze[ni][nj] == 'F' or (ni,nj) in visited:
            while visited:
                a, b = visited.pop()
                maze[a][b] = 'F'
            return 0
        # 아니면 더 돌아
        elif 0<=ni<N and 0<=nj<M:
            i,j = ni,nj

N, M = map(int,input().strip().split())
maze = [list(input().strip()) for _ in range(N)]
# 답 카운트
cnt = 0
for i in range(N):
    for j in range(M):
        cnt += runaway(maze,i,j)
print(cnt)