# 1. 2부터 루트 N 까지의 소수 구하기
# 2. 소인수분해 실행
import time
start = time.time()

N = int(input())
M = int(N**1/2)

# N의 반까지 소수 구하기
check = [1, 1] + [0] * (M - 1)
semi_divisor = []
for i in range(2, int(M ** 1 / 2) + 1):
    if check[i] != 1:
        for j in range(2 * i, M + 1, i):
            check[j] = 1

for p in range(len(check)):
    if check[p] == 0:
        semi_divisor.append(p)

semi_divisor.append(N)

cnt = 0
while N != 1:
    if N % semi_divisor[cnt] == 0:
        print(semi_divisor[cnt])
        N = N / semi_divisor[cnt]
    else:
        cnt += 1

end = time.time()
print(f"{end - start:.5f} sec")


'''
def soinsu(num, i=0):
    if num:
        return None

    elif num % semi_divisor[i] == 0:
        print(semi_divisor[i])
        return soinsu(num/i,i)

    else:
        return soinsu(num,i+1)
        
soinsu(N)
'''