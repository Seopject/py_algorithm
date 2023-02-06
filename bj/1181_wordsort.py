N = int(input())
words = [0]*N
for i in range(N):
    words[i] = input()
words = set(words)
words = list(words)
words.sort()
words.sort(key=lambda x:len(x))
for i in words:
    print(i)