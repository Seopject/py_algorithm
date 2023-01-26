is_input = input().lower()
word = list(is_input)

# 알파벳 리스트
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

alpha_cnt = [0]*26

for i in word:
    alpha_cnt[alphabet.index(i)] += 1

if alpha_cnt.count(max(alpha_cnt)) > 1:
    print('?')

elif alpha_cnt.count(max(alpha_cnt)) == 1:
    print(alphabet[alpha_cnt.index(max(alpha_cnt))].upper())