C = int(input()) # TC
for tc in range(C):
    scorelist = list(map(int, input().split()))
    num_of_students = scorelist[0]
    scores = scorelist[1:]
    avg = (sum(scores)/num_of_students)
    avg_cnt = 0
    for i in scores:
        if i > avg:
            avg_cnt += 1
    answer = '{:.3f}%'.format(avg_cnt/num_of_students*100)
    print(answer)