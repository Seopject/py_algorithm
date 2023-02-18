from itertools import combinations

txt = input()
stack = []
brkt = []
for i in range(len(txt)):
    if txt[i] == '(':
        stack.append(i)
    elif txt[i] == ')':
        brkt.append([stack.pop(),i])

result = set()
for i in range(len(brkt)):
    k = combinations(brkt,i+1)
    for j in k:
        ans = list(txt)
        for x in j:
            ans[x[0]] = ''
            ans[x[1]] = ''
            result.add(''.join(ans))

for i in sorted(list(result)):
    print(i)
