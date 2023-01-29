def answer(X,find,dn):
    if find >= X:
        return (X, find, dn)

    find += dn
    dn += 1
    return answer(X, find, dn)

print(answer(500,1,2))

'''
def locations(X,x,y,cnt):
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


print(locations(int(input()),1,1,1)
'''



""" 
X = int(input())
location = [1]*2
cnt = 1
for _ in range(1, X):
    if location[1] == 1:
        location = location[::-1]
        location[1] += 1
    else:
        location[0] += 1
        location[1] -= 1
    cnt += 1       

print(f'{location[0]}/{location[1]}')

 """
    