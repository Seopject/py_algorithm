tc = list(input())

# 다이얼 딕셔너리
a = {
    2 : ['A', 'B', 'C'],
    3 : ['D', 'E', 'F'],
    4 : ['G', 'H', 'I'],
    5 : ['J', 'K', 'L'],
    6 : ['M', 'N', 'O'],
    7 : ['P', 'Q', 'R', 'S'],
    8 : ['T', 'U', 'V'],
    9 : ['W', 'X', 'Y', 'Z']
}
cnt = 0
for i in range(2, 10):
    for j in range(len(a[i])):
        for k in tc:
            if k == a[i][j]:
                cnt += i+1

print(cnt)