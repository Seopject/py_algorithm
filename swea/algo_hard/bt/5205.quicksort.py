def quickbuthard(A,left,right):
    pivot = A[left]
    i = left
    j = right
    while i <= j:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] > pivot:
            j -= 1
        if i<j:     # 이걸 못만나
            A[i], A[j] = A[j], A[i]

    A[j], A[left] = A[left], A[j]
    return j

def sorting(A,left,right):
    if left < right:
        m = quickbuthard(A,left,right)
        sorting(A,left,m-1)
        sorting(A,m+1,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    sorting(arr,0,N-1)

    answer = arr[N//2]
    print(f'#{tc} {answer}')