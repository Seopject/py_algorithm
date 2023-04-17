import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input().rstrip()))
arr = deque(arr)

ans = 0

while arr:
    temp = arr.popleft()
    print(temp)
