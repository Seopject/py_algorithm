def pre(n):
    if n != '.':
        print(n, end = '')
        pre(dict[n][0])
        pre(dict[n][1])

def mid(n):
    if n != '.':
        mid(dict[n][0])
        print(n, end='')
        mid(dict[n][1])

def post(n):
    if n != '.':
        post(dict[n][0])
        post(dict[n][1])
        print(n, end='')

N = int(input())
dict = {}
for i in range(N):
    p, c1, c2 = input().split()
    dict[p] = c1,c2

pre('A')
print()
mid('A')
print()
post('A')
print()