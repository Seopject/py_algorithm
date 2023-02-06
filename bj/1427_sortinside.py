N = sorted(list(map(str, input())), reverse=True)
k = N[0]
for i in range(1, len(N)):
    k += N[i]
print(int(k))