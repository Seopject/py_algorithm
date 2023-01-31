# 1. 2부터 루트 N 까지의 소수 구하기
# 2. 소인수분해 실행

N = int(input())

# 소수 구하기
cnt = 0
check = []
for j in range(1, int(N**1/2)+1):
    if N % j == 0:
        check.append(j)
if len(check) == 1:
        cnt += 1

print(check)


""" N = int(input())
# 소인수분해
def soinsu(num, i=2):
    if num == 1:
        return None

    elif num % i == 0:
        print(i)
        return soinsu(num/i,i)

    else:
        return soinsu(num,i+1)
        
soinsu(N) """