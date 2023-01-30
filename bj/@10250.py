T = int(input()) #tc
for _ in range(T):
    height, width, customer = list(map(int, input().split()))

    if customer % height == 0:
        line = customer // height
        floor = height
    else:
        line = (customer // height) + 1
        floor = customer % height

    print(str(floor) + str(line).zfill(2))
    
# zfill -> 자리수만큼 0 채우기    