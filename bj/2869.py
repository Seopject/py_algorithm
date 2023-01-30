import math
# A 낮에 달팽이 올라가는 거리
# B 밤에 미끄러지는 걸
# V 막대의 높이
A, B, V = list(map(int, input().split()))
if (A-B) == 1:
    print(V - B)
else:
    print(math.ceil((V-B)/(A-B)))