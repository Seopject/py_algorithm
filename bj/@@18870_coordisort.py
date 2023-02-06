# 서로 다른 좌표의 수
# sort해서 맨 첫번째 해당하는 i 값의 -1
N = int(input())
coor = list(map(int, input().split()))
coorsort = sorted(list(set(coor)))
temp = {}
for i in range(len(coorsort)):
    temp[coorsort[i]] = i

for i in range(N):
    print(temp[coor[i]], end=' ')