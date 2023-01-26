# 변수끼리의 복사
a = 10
b = a
b = 20
print(a)
# 복사 후 값 변경해도 원본 값 유지 -> 깊은 복사(deep copy)
# 주소가 아닌 값을 복사하는 경우

# 함수에서의 복사
def func(num):
    num += 10
    return num

n = 10
func(n) # 깊은 복사가 일어난다면 -> 10 출력, 기존 n에 영향 X
        # 얕은 복사가 일어난다면 -> 20
print(n)
print(func(n))