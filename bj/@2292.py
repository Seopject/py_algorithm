tc = (int(input()) - 1)/6

# 수열 리스트
d_list = [0,0]

cnt = 0

while True:
    d_list[1] = d_list[0] + (cnt + 1) # [0,1] -> [1,]
    if tc == 0:
        print(1)
        break
    elif tc > 0 and tc <= 1/6:
        print(2)
        break
    elif tc > d_list[0] and tc <= d_list[1]:
        print(cnt+2)
        break
    else:
        d_list[0] = d_list[1]
        cnt += 1
