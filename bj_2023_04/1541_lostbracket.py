arr = input().split('-')
ans = 0
for temp in arr[0].split('+'):
    ans += int(temp)
for temp in arr[1:]:
    for temp2 in temp.split('+'):
        ans -= int(temp2)

print(ans)