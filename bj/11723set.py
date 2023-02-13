import sys
input = sys.stdin.readline
S = set()
M = int(input()) # 연산 수
for i in range(M):
    order = input().split()
    if order[0] == 'add' and order[1] not in S:
        S.add(order[1])
    elif order[0] == 'remove' and order[1] in S:
        S.remove(order[1])
    elif order[0] == 'check':
        if order[1] in S:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == 'all':
        S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif order[0] == 'empty':
        S = set()