T = int(input())
for tc in range(1,T+1):
    str1 = list(input())
    cnt = [0]*len(str1)
    str2 = list(input())
    maxV = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                cnt[i] += 1
    print(f'#{tc} {max(cnt)}')