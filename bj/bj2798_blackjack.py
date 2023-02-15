N,M = map(int,input().split())
card = list(map(int,input().split()))
ans = -1
for a in range(len(card)-2):
    for b in range(a+1,len(card)-1):
        for c in range(b+1,len(card)):
            if card[a]+card[b]+card[c] <= M and card[a]+card[b]+card[c] > ans:
                ans = card[a]+card[b]+card[c]

print(ans)
