# N까지 자연수까지 M 길이 수열, 중복 없이

def combi(idx,list):    # 조합 재귀
    if len(list) == M:
        print(*list)
        return
    for i in range(idx,len(arr)):
        combi(i+1,list+[arr[i]])

N, M = map(int,input().split())
arr = list(range(1,N+1))
idx = 0
ans = []
combi(idx,[])