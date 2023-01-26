tc = int(input())

for i in range(tc):
    quiz = list(input())
    totalscore = 0
    score = 0
    for k in quiz:
        if k == 'O':
            score += 1
            totalscore += score
        else:
            score = 0
    print(totalscore)