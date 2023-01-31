N = int(input())
check = [0] * N
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