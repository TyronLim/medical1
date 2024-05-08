class Car:
    value = '부모의 값 1'
    def car_func(self):
        print('1. 부모의 값을 출력합니다.')
        
class Am(Car):
    value = '자식의 값 2'
    def car_func(self):
        print('2. 자식의 값을 출력합니다.')
        super().car_func()  # 부모 값 호출
        print('3. 자식클래스 안에 있는 부모의 값 :', super().value)
        print('4. 자식클래스 안에 있는 자식의 값 :', self.value)
        
a1 = Am()
a1.car_func()


class As:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.v = c
        
        
a1 = As()