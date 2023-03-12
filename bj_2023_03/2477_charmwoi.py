K = int(input())
cnt = [[] for _ in range(5)]    # 동서남북
total = []
line = []

for i in range(6):
    dir, val = map(int,input().split())
    cnt[dir].append(val)
    line.append((dir,val))

for i in range(1,5):
    if len(cnt[i]) == 1:
        total.append(cnt[i][0])

part = []
for i in range(6):
    if line[i-1][0] == line[(i+1)%6][0]:
        part.append(line[i][1])

ans = abs(total[0]*total[1]) - abs(part[0]*part[1])
print(ans*K)