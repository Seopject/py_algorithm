N = int(input()) # N까지
cnt = 0 # 한수 count

for tc in range(1, N+1):
    tc = list(map(int, str(tc))) # 입력 수 리스트화
    dim_list = []

    # 한자리수 검증
    if len(tc) == 1:
        cnt += 1

    else:
        for j in range(len(tc)-1):
            dim_list.append(int(tc[j])-int(tc[j+1]))
        if len(set(dim_list)) == 1:
            cnt += 1

print(cnt)