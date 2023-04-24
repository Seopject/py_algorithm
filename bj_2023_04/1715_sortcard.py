import heapq
import sys

input = sys.stdin.readline

N = int(input())
Q = []
for i in range(N):
    heapq.heappush(Q, int(input()))

ans = 0

if N == 1:
    print(0)

else:
    for i in range(N-1):
        front = heapq.heappop(Q)
        back = heapq.heappop(Q)
        ans += (front+back)
        heapq.heappush(Q,front+back)

    print(ans)