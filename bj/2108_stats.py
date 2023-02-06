# 음수가 있다면...
# 1~50만 절대값이라면 100만까지 만들고 -1, -2 슬라이싱
N = int(input()) # tc
num = [0] * 8001
numlist = [0]*N
for i in range(N):
    k = int(input())
    num[k] += 1
    numlist[i] = k
numlist.sort()
# 산술평균
print(round(sum(numlist)/N))
# 중앙값
print(numlist[N//2])
# 최빈값
if num.count(max(num)) == 1:
    if num.index(max(num)) > 4000:
        print(num.index(max(num)) - 8001)
    else:
        print(num.index(max(num)))
else:
    temp = []
    for i in range(4001,8001):
        if num[i] == max(num):
            temp.append(i-8001)
    for j in range(4001):
        if num[j] == max(num):
            temp.append(j)
    print(temp[1])
# 범위
print(max(numlist)-min(numlist))