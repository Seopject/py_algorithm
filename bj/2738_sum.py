N, M = map(int, input().split()) # N개 줄에 원소 M개
temp1 = []
temp2 = []
for i in range(N):
    temp1 += map(int, input().split())

for i in range(N):
    temp2 += map(int, input().split())

for i in range(N*M):
    temp1[i] = temp1[i] + temp2[i]

for i in range(N):
    print(*temp1[M*i:M*(i+1)])