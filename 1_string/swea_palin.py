T = int(input())
for tc in range(1,T+1):
    target = input()
    mirroring = target[::-1]
    if target == mirroring:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')