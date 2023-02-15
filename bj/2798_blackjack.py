N, M = map(int, input().split()) # N : 카드 개수, M : 대상 수
card = list(map(int, input().split()))
# M을 넘지 않고 최대한 가까운 카드 3장
ans = -1
for i in range(N):
    for j in range(i,N):
        print(sum(card[i:j+1]))
        if sum(card[i:j+1]) <= M and ans < sum(card[i:j+1]):
            ans = sum(card[i:j+1])

print(ans)