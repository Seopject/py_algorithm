import sys
input = sys.stdin.readline

symbol = {
    0 : '+',
    1 : '-',
    2 : '*',
    3 : '//',
}

def calc(p,i):
    temp = [arr[0]]
    for t in range(i):
        temp.append(p[t])
        temp.append(arr[t + 1])
        if temp[1] == '//' and int(temp[0]) < 0 and int(temp[2]) > 0:
            temp[0] = str(int(temp[0]) * -1)
            temp = [str(eval(''.join(temp)))]
            temp[0] = str(int(temp[0]) * -1)
        else:
            temp = [str(eval(''.join(temp)))]

    return int(temp[0])


def perm(i,k):
    global minans, maxans

    if i == k:
        if ''.join(p) not in visited:
            visited[''.join(p)] = True
            temp = calc(p,k)
            minans = min(minans,temp)
            maxans = max(maxans, temp)

    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = oper[j]
                used[j] = 1
                perm(i+1,k)
                used[j] = 0


N = int(input())
arr = list(map(str,input().rstrip().split()))
op = list(map(int,input().rstrip().split()))
minans = 1000000000
maxans = -1000000000

oper = []
for i in range(4):
    if op[i] > 0:
        for k in range(op[i]):
            oper.append(symbol.get(i))

p = [0]*(N-1)
used = [0]*(N-1)
visited = {}
perm(0,N-1)

print(maxans)
print(minans)
