N = int(input())
members = [0]*N
for i in range(N):
    members[i] = input().split()
members.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(*members[i])