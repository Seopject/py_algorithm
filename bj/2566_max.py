numlist = []
for i in range(9):
    numlist += map(int, input().split())

print(max(numlist))
print((numlist.index(max(numlist))//9)+1, (numlist.index(max(numlist))%9)+1)