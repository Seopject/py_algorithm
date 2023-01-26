def d(n):
    dlist = list(map(int, str(n)))
    return n + sum(dlist)

dnlist = []
for i in range(1, 10001):
    dnlist.append(d(i))

for j in range(1, 10001):
    if j not in dnlist:
        print(j)