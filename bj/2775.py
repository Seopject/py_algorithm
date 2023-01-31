# 403호에 살려면 301~303호까지 사람들의 수 합만큼 사람들을 데려와 살아야한다
# k와 n에 대해 k층 n호에 몇 명이 살고있는가 아파트 0층부터, 1호부터
# 0층 i호는 i명이 산다

T = int(input()) # tc
for tc in range(T):
    floor = int(input()) # 층수
    num = int(input()) #호수

    floorlist_up = [0]*num
    floorlist_down = list(range(1,num+1))

    for n in range(floor):
        for k in range(num):
            floorlist_up[k] = sum(floorlist_down[0:k+1])
        floorlist_down = floorlist_up
        floorlist_up = [0]*num

    print(floorlist_down[num-1])

