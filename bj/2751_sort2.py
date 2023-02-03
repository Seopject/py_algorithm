N = int(input()) # 수 개수
num = [0]*N
for i in range(N):
    num[i] = int(input())
num.sort()
print(num)