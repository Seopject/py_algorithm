T = int(input())
for tc in range(1,T+1):
    bin = list(input())
    ter = list(input())

    for i in range(len(bin)):
        bin[i] = str((int(bin[i]) + 1)%2)
        for j in range(len(ter)):
            for k in range(2):
                ter[j] = str((int(ter[j]) + 1) % 3)

                if int(''.join(bin),2) == int(''.join(ter),3):
                    answer = int(''.join(bin),2)
                    print(f'#{tc} {answer}')

            ter[j] = str((int(ter[j]) + 1) % 3)
        bin[i] = str((int(bin[i]) + 1)%2)