# 일차함수 그리고 생각하기
import math

# 단위 : 만원
A, B, C = list(map(int, input().split()))

# 노트북 판매대수
cnt = 0

if (C - B) <= 0:
    print(-1)
else:
    print(math.floor(A/(C-B))+1)