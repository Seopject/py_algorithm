# 시간초과
import sys
input = sys.stdin.readline
rule = { 'U' : (-1,0), 'R' : (0,1), 'D' : (1,0), 'L' : (0,-1)}
def runaway(maze,i,j): # maze, i,j 입력
    while True:
        visited[i][j] = 1
        ni,nj = i+rule.get(maze[i][j])[0], j+rule.get(maze[i][j])[1]
        # 나가면 1 리턴
        if ni<0 or ni>N-1 or nj<0 or nj>M-1:
            return 1
        elif visited[ni][nj] == 1:
            return 0
        # 아니면 더 돌아
        elif 0<=ni<N and 0<=nj<M:
            i,j = ni,nj

N, M = map(int,input().split())
maze = [list(input().strip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 답 카운트
cnt = 0
for i in range(N):
    for j in range(M):
        cnt += runaway(maze,i,j)
print(cnt)
