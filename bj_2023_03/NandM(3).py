import itertools
# N까지 자연수까지 M 길이 수열, 중복 없이

N, M = map(int,input().split())
arr = list(range(1,N+1))
ans = list(itertools.permutations(arr,M))
for i in range(len(ans)):
    print(*ans[i])