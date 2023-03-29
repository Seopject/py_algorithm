import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr)+1)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    temp = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            temp.append(left[l])
            ans.append(left[l])
            l += 1

        else:
            temp.append(right[r])
            ans.append(right[r])
            r += 1


    while l < len(left):
        temp.append(left[l])
        ans.append(left[l])
        l += 1


    while r < len(right):
        temp.append(right[r])
        ans.append(right[r])
        r += 1

    return temp

N, K = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
ans_list = merge_sort(arr)

if len(ans) < K:
    print(-1)
else:
    print(ans[K-1])