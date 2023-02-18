N = int(input())
A = set(map(int, input().split()))
M = int(input())
num = list(map(int,input().split()))
for tc in num:
    if tc in A:
        print(1)
    else:
        print(0)