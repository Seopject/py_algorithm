T = int(input()) # 반복할 수

for tc in range(T):
    # input
    origin_input = list(map(str, input()))
    times = int(origin_input[0])
    words = origin_input[2:]
    
    # 답
    answer = ''
    for i in words:
        answer += i*times
    print(answer)