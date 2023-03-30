import sys
sys.stdin = open('input_m.txt','r')

def igedaechemerge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2

    left = igedaechemerge(arr[:mid])
    right = igedaechemerge(arr[mid:])

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

arr=list(map(int,input().split()))
arr = igedaechemerge(arr)
print(arr[500000])
