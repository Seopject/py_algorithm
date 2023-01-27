N = int(input()) # 단어의 개수
cnt = 0
for tc in range(N):
    word = list(input())
    verify = []

    # 2글자 이하는 다 맞는듯
    if len(word) <= 2:
        pass

    else:
        for i in range(len(word)):
            if i < 2:
                verify.append(word[i])

            else:
                # 앞에서 안나온거면 추가
                if word[i] not in verify:
                    verify.append(word[i])
                # 앞에 있었으면 검증
                elif word[i] in verify and word[i-1] == word[i]:
                    verify.append(word[i])
                    pass
                elif word[i] in verify and word[i-1] != word[i]:
                    N -= 1
                    break
            cnt += 1
                       
print(N)
