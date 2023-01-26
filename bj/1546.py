N = int(input()) # 시험 본 과목 수
score = list(map(int, input().split()))
lie = max(score)

for i in range(len(score)):
    score[i] = score[i]/lie*100

print(sum(score)/len(score))