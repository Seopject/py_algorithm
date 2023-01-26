S = input() # 알파벳 소문자로만 이루어진 단어 S 입력
word = list(S)

# 알파벳 리스트
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

# 답
answer = []
for j in alphabet:
    if j in word:
        answer.append(word.index(j))
    else:
        answer.append(-1)

print(*answer)