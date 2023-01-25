tc = int(input()) # 26
answer = tc
cnt = 0
def cycle(num):
    global cnt, answer

    if num//10 == 0:
        A = '0'
        B = str(num)
        num = int(B + str((int(A)+int(B))%10))

    else:
        A = list(str(num))[0]
        B = list(str(num))[-1]
        num = int(B + str((int(A)+int(B))%10))

    cnt += 1

    if num == answer:
        return(print(cnt))

    else:
        cycle(num)

cycle(tc)