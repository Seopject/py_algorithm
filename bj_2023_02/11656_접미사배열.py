txt = input()
ans = [0]*len(txt)
for i in range(len(txt)):
    ans[i] = txt[i:]
for i in range(len(ans)):
    print(sorted(ans)[i])