N = int(input()) # 수 개수
num = [0]*1000001
for i in range(N):
    num[int(input())] += 1
for i in range(N):
    print(num[i])