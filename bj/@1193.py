import sys
limit_num = 5000
sys.setrecursionlimit(limit_num)

def answer(X,find,dn):
    if find >= X:
        return (X, find, dn)

    find += dn
    dn += 1
    return answer(X, find, dn)

X, find, dn = list(answer(int(input()),1,2))

if (dn-1)%2 == 0:
    print(f'{(dn-1) - (find - X)}/{1 + (find - X)}')
else:
    print(f'{1 + (find - X)}/{(dn-1) - (find - X)}')


# dn-1 번째 줄에 있다
# dn-1/1에서 오른쪽 위로 find - X 만큼 가야함
# (dn-1) - (find - X) / 1 + (find - X)

#1 3 6 10 15 21 28

""" def locations(X,x,y,cnt):
    location = [x,y]
    if X == cnt:
        return f'{x}/{y}'

    elif location[1] == 1:
        location = location[::-1]
        location[1] += 1
        cnt += 1
        x, y = location[0], location[1]
        return locations(X,x,y,cnt)
    else:
        location[0] += 1
        location[1] -= 1
        cnt += 1
        x, y = location[0], location[1]
        return locations(X,x,y,cnt)

print(locations(9000,1,1,1))

 """
