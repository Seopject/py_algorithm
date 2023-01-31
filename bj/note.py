class Person:
    def __init__(self):
        self._age = 0
        #protected
    
    @property
    def age(self): #getter
        print('getter 호출 !')
        return self._age
    
    @age.setter
    def age(self, age): #setter
        print('setter 호출 !')
        self._age = age

    # 데코레이터 없을 때
    # age = property(get_age, set_age)
    
    
p1 = Person()
# p1._age = 25 #protect에선 사용하면 안됨

# 비교적 불편
""" p1.set_age(25)
print(p1.get_age())
 """
# 내부적으로 setter, getter 사용
p1 = Person()
p1.age = 25
print(p1.age)