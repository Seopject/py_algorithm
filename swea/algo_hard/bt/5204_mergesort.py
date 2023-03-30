def igedaechemerge(arr):
    global answer

    if len(arr) < 2:
        return arr

    mid = len(arr)//2

    left = igedaechemerge(arr[:mid])
    right = igedaechemerge(arr[mid:])
    if left[-1] > right[-1]:
        answer += 1

    mergearr = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            mergearr.append(left[l])
            l += 1
        else:
            mergearr.append(right[r])
            r += 1
    mergearr += left[l:]
    mergearr += right[r:]
    return mergearr


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    temp = [0]*N
    answer = 0
    num = igedaechemerge(num)
    print(f'#{tc} {num[N//2]} {answer}')