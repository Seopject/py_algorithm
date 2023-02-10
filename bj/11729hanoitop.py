def hanoi(N,arr1,arr2,arr3): # N = 개수
    cnt = 0
    # 끝 조건
    if len(arr3) == N:
        return None

    # 홀수라면
    if N % 2:
        pass

N = int(input())
arr1 = [0]*N
arr2 = [0]
arr3 = [0]
for i in range(N):
    arr1[i] = i+1

print(arr2 == [] or arr1[1] > arr2[0])
print(len(arr3))
print(max(arr2))