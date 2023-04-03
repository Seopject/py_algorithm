part_range = [[0,3],[-1,2],[-2,1]]

import sys
input = sys.stdin.readline

def is_row_col(t,r,c):
    for i in range(9):
        if arr[r][i] == t:
            return False
        if arr[i][c] == t:
            return False

    tr, tc = r%3, c%3
    for i in range(r+part_range[tr][0],r+part_range[tr][1]):
        for j in range(c+part_range[tc][0],c+part_range[tc][1]):
            if arr[i][j] == t:
                return False
    return True

def func(i,N):
    if i == N:
        for r in range(9):
            print(*arr[r])
        exit(0)

    else:
        r, c = blank[i]
        for t in range(1,10):
            if is_row_col(t,r,c):
                arr[r][c] = t
                func(i+1,N)
                arr[r][c] = 0

arr = [list(map(int,input().rstrip().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))
N = len(blank)
func(0,N)
