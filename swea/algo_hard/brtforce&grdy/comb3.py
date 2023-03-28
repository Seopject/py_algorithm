
# p : 데이터가 저장된 배열
# k : 원소의 개수
# i : 선택된 원소의 수

def comb(i, k, last):
    if i == k:
        print(*p)
    else:
        for j in range(last+1, n):
            p[i] = A[j]
            comb(i+1, k, j)

n = 5
A = [1,2,3,4,5]
k = 3
p = [0]*k
comb(0, k, -1)

