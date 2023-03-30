import sys
sys.stdin = open('input_m.txt','r')

def partition(A,l,r):
    pivot = A[l]
    i, j = l, r
    while i<=j:     # i 가장 왼쪽에 있는 피봇보다 큰 값
                    # j 가장 오른쪽에 있는 피봇보다 작은 값 들을 찾는 인덱스
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i<j:
            A[i], A[j] = A[j], A[i]     # 피봇보다 큰 값이 작은 값 왼쪽에 있는 경우 교환
    A[j], A[l] = A[l], A[j]             # 피봇 값을 경계에 위치
    return j                            # 피봇의 위치를 리턴

def qsort(A,l,r):
    if l < r:
        s = partition(A,l,r)
        qsort(A,l, s-1)     # 피봇보다 작은 값 (피봇 왼쪽)
        qsort(A,s+1,r)      # 피봇보다 큰 값 (피봇 오른쪽)

arr = list(map(int,input().split()))
qsort(arr,0,999999)
print(arr[500000])


