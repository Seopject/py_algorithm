while True:
    N = list(input())
    if N == ['0']:
        break
    if N == N[::-1]:
        print('yes')
    else:
        print('no')