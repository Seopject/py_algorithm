N = int(input()) # 수의 개수
numbers = list(map(int, input().split()))
cnt = 0

for i in numbers:
    check = []
    for j in range(1, int(i**1/2)+1):
        if i % j == 0:
            check.append(j)
    if len(check) == 1:
        cnt += 1

print(cnt)